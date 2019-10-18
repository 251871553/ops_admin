from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.apis import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
import  sys


def exec_commands(api_instance):
    name = 'oms4-sales-order-manager-5f7bd865cf-8fvng'
    resp = None
    try:
        resp = api_instance.read_namespaced_pod(name=name,
                                                namespace='prod')
    except ApiException as e:
        if e.status != 404:
            print("Unknown error: %s" % e)
            exit(1)
    if not resp:
        print("Pod %s does not exist." % name)
    # Calling exec and waiting for response
    #sys.exit()
    container_cmd="pgrep java | xargs jstack -l >>/tmp/oms4-sales-order-manager-75ffcddcfb-6cnc4.prof && ls -l /tmp"
    #container_cmd='curl -H "Content-Type: multipart/form-data"   http://10.45.24.134:8001/api/upload/ -F "file=@/tmp/oms4-sales-order-manager-75ffcddcfb-6cnc4.prof"'
    print(container_cmd)
    #sys.exit()
    exec_command = ['/bin/sh', '-c', container_cmd]
    resp = stream(api_instance.connect_get_namespaced_pod_exec,
                  name,
                  'prod',
                  command=exec_command,
                  stderr=True, stdin=False,
                  stdout=True, tty=False)
    print("Response: " + resp)
    #resp.close()
def main():
    #config.load_kube_config()
    config.kube_config.load_kube_config(config_file="./config/kubeconfig.yaml")  #django path is diffrent
    c = Configuration()
    c.assert_hostname = False
    Configuration.set_default(c)
    core_v1 = core_v1_api.CoreV1Api()

    exec_commands(core_v1)


if __name__ == '__main__':
    main()