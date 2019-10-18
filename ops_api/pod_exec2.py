import time

from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.apis import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
import  sys
def exec_commands(api_instance):
    name = 'oms4-sales-order-manager-75ffcddcfb-6cnc4'
    resp = None
    try:
        resp = api_instance.read_namespaced_pod(name=name, namespace='prod')
    except ApiException as e:
        if e.status != 404:
            print("Unknown error: %s" % e)
            exit(1)
    if not resp:
        print("Pod %s does not exist." % name)
    exec_command = ['/bin/sh']
    resp = stream(api_instance.connect_get_namespaced_pod_exec,
                  name,
                  'prod',
                  command=exec_command,
                  stderr=True, stdin=True,
                  stdout=True, tty=False,
                  _preload_content=False)
    commands = [
        "ps aux | grep java | grep  -v grep | awk '{print $1}'| xargs jstack -l",
        "echo \"This message goes to stderr\" >&2",
    ]
    while resp.is_open():
        resp.update(timeout=1)
        if resp.peek_stdout():
            print("STDOUT: %s" % resp.read_stdout())
        if resp.peek_stderr():
            print("STDERR: %s" % resp.read_stderr())
        if commands:
            c = commands.pop(0)
            print("Running command... %s\n" % c)
            resp.write_stdin(c + "\n")
        else:
            break
    #resp.write_stdin("date\n")
    resp.write_stdin("ps aux | grep java | grep  -v grep | awk '{print $1}'| xargs jstack -l\n")
    app_pid = resp.readline_stdout(timeout=3)
    print(app_pid)
    #resp.write_stdin("ps aux | grep %s\n" % app_pid)
   # resp.write_stdin("jstack -l %s > /tmp/22.log\n" % app_pid)
    #jstack = resp.readline_stdout(timeout=5)
   # print(jstack)
    resp.close()
def main():
    #config.load_kube_config()
    config.kube_config.load_kube_config(config_file="./config/kubeconfig.yaml")
    c = Configuration()
    c.assert_hostname = False
    Configuration.set_default(c)
    core_v1 = core_v1_api.CoreV1Api()

    exec_commands(core_v1)

if __name__ == '__main__':
   main()