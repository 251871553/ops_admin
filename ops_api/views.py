from django.shortcuts import render,redirect,reverse
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import os
import sys
import logging
from ops_api.k8s_api import k8s_api


my_k8s=k8s_api('prod')

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

@csrf_exempt
def index(request):
    if request.method == "GET":
        return HttpResponse('success')
    elif request.method == "POST":
        print(request.body)
        print(request.content_type)
        #print(request.get_host())
        #print(request.META['REMOTE_ADDR'])
        #print(request.META)
        if request.content_type == "application/json":
           #print(request.body)
           req = json.loads(request.body)
           return HttpResponse(json.dumps({'code': 0, 'message': 'ok'}))
        elif request.content_type == 'application/x-www-form-urlencoded':
           return HttpResponse('success')
        elif request.content_type == 'application/octet-stream':
           return HttpResponse('octet-stream')
        elif request.content_type == 'multipart/form-data':
            return HttpResponse('multipart/form-data')
        else:
           print(request.content_type)
           print(request.body)
        return HttpResponse('success')
    else:
        return HttpResponse(json.dumps({'code': 1, 'message': 'request model error'}))

@csrf_exempt
def form_analysis(request):
    if request.method == 'POST':
       pod_ipaddr=request.POST.get('ip_addr', None)
       #print(pod_ipaddr)
       logging.info(pod_ipaddr)
    return HttpResponse('success')

@csrf_exempt
def k8s_api(request):
    if request.method == 'POST':
       pod_ipaddr=request.POST.get('ip_addr', None)
       logging.info(pod_ipaddr)
       #print(pod_ipaddr)
       #print(os.path.exists('ops_api/config'))
       #print(os.getcwd())
       #my_k8s.jstack_jvm('10.160.135.186')
       if my_k8s.jstack_jvm(pod_ipaddr) == 0:
    #return HttpResponse('success')
    #return redirect('http://10.45.24.134:8001/www/files/')
          return HttpResponseRedirect('http://10.45.24.134:8001/www/files/')
       else:
          return HttpResponse('pod not exits')


#处理上传文件
@csrf_exempt
def upload_file(request):
    if request.method == "GET":
        return HttpResponse('bad request mode')
    elif request.method == "POST":
        if request.content_type == 'multipart/form-data':
            myfile = request.FILES.get('file', None)

            if not myfile:
                return HttpResponse("no files for upload!")
            #print(os.getcwd())
            # filesize=myfile.size
            logging.info(myfile.name)
            #print('here')
            logging.info(round(myfile.size/1024))
            destination = open(os.path.join("ops_api/upload_files", myfile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
            if myfile.multiple_chunks() == False:
                destination.write(myfile.read())  # 小于2.5M
                logging.info('小于2.5M')
            else:
                logging.info('大文件')
                for chunk in myfile.chunks():  # 分块写入文件
                    destination.write(chunk)
            destination.close()
            return HttpResponse("upload over!")
    else:
        return HttpResponse(json.dumps({'code': 1, 'message': 'request model error'}))