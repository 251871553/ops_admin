from kubernetes import client, config
from kubernetes.client import Configuration
from kubernetes.client.apis import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
import warnings
warnings.filterwarnings("ignore")
import redis
import  logging
import sys


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
r = redis.Redis(host='10.11.6.150', port=6379, db=0)
#config.kube_config.load_kube_config()
#sys.exit()
config.kube_config.load_kube_config(config_file="ops_api/config/kubeconfig.yaml")
v1 = client.CoreV1Api()


class k8s_api:
    def __init__(self, pod_namespace):
        self.pod_namespace = pod_namespace

    def get_version():
        print("Supported APIs (* is preferred version):")
        print("%-40s %s" %
              ("core", ",".join(client.CoreApi().get_api_versions().versions)))
        for api in client.ApisApi().get_api_versions().groups:
            versions = []
            for v in api.versions:
                name = ""
                if v.version == api.preferred_version.version and len(
                        api.versions) > 1:
                    name += "*"
                name += v.version
                versions.append(name)
            print("%-40s %s" % (api.name, ",".join(versions)))

    def pod_list(self):
        ret = v1.list_namespaced_pod(namespace=self.pod_namespace, watch=False)
        pod_dict = {}
        for i in ret.items:
            # print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
            pod_dict[i.status.pod_ip] = i.metadata.name
        r.hmset(self.pod_namespace, pod_dict)

    #def pod_search(self, pod_ip):
     #   result=r.hget(self.pod_namespace, key=pod_ip)
     #   return result


    def exec_commands(self, api_instance,pod_ip):
        result = r.hget(self.pod_namespace, key=pod_ip)
        if not result:
           self.pod_list()
           logging.warning('update redis')
        result2 = r.hget(self.pod_namespace, key=pod_ip)
        if result2:
           pod_name = result2
        else:
           logging.error('pod not exits')
           return 1
        pod_name = bytes.decode(pod_name)
        resp = None
        try:
            resp = api_instance.read_namespaced_pod(name=pod_name, namespace=self.pod_namespace)
        except ApiException as e:
            if e.status != 404:
                #print("Unknown error: %s" % e)
                logging.error("Unknown error: %s" % e)
                #exit(1)
                return 1
        if not resp:
            #print("Pod %s does not exist." % pod_name)
            logging.error("Pod %s does not exist." % pod_name)
            return 1

        container_cmd = 'pgrep java | xargs jstack -l > /tmp/%s.prof && curl -# -H "Content-Type: multipart/form-data" http://10.45.24.134:8001/api/upload/ -F "file=@/tmp/%s.prof"' % (pod_ip,pod_ip)
        logging.info(container_cmd)
        exec_command = ['/bin/sh', '-c', container_cmd]
        resp = stream(api_instance.connect_get_namespaced_pod_exec,
                      pod_name, self.pod_namespace, command=exec_command,
                      stderr=True, stdin=False,
                      stdout=True, tty=False)
        #print("Response: " + resp)
        logging.info(resp)
        return 0

    def jstack_jvm(self, pod_ip):
        c = Configuration()
        c.assert_hostname = False
        Configuration.set_default(c)
        core_v1 = core_v1_api.CoreV1Api()
        #print('zzzzzzzzzz')
        if self.exec_commands(core_v1, pod_ip) == 0:
           return 0
        else:
           return 1

    def __del__(self):
        pass

if __name__ == '__main__':
    pass
   # my_k8s=k8s_api('prod')
    #my_k8s.jstack_jvm('10.160.131.202')