from kubernetes import client, config
import warnings
warnings.filterwarnings("ignore")

import redis
r=redis.Redis(host='10.11.6.150', port=6379, db=0)



#pip install redis==2.10.6

config.kube_config.load_kube_config(config_file="./config/kubeconfig.yaml")

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
#ret = v1.list_pod_for_all_namespaces(watch=False)
ret=v1.list_namespaced_pod(namespace='prod', watch=False)
pod_dict={}
for i in ret.items:
    #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    pod_dict[i.status.pod_ip]=i.metadata.name
    #r[i.status.pod_ip]=i.metadata.name
    #print(type(i.status.pod_ip))
    #print(type(i.metadata.name))
    #r.set(i.status.pod_ip,i.metadata.name)
    #r.hset('prod',str(i.status.pod_ip),str(i.metadata.name))
#print(pod_dict)
r.hmset('prod', pod_dict)





