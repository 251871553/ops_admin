from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import StreamingHttpResponse
import os,sys
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('www/index.html')
    context = {
        'latest_question_list': 'hello',
    }
    return HttpResponse(template.render(context, request))

def welcome(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('www/welcome.html')
    context = {
        'latest_question_list': 'hello',
    }
    return HttpResponse(template.render(context, request))

def login(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('www/login.html')
    context = {
        'latest_question_list': 'hello',
    }
    return HttpResponse(template.render(context, request))

def demo(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('www/mytest.html')
    context = {
        'latest_question_list': 'hello',
    }
    return HttpResponse(template.render(context, request))

def dump(request):
    template = loader.get_template('www/pod_info.html')
    context = {
        'latest_question_list': 'hello',
    }
    return HttpResponse(template.render(context, request))

def files(request):
    #return HttpResponse('xxx')
    #context = {'file_list': 'abc.prof'}
    #print(os.path.isdir('ops_api/upload_files'))
    #a=os.listdir('ops_api/upload_files')
    file_path = 'ops_api/upload_files/'
    file_list = os.listdir(file_path)
    #print(c)
    file_info = {}
    for filename in file_list:
        #    print(i)
        full_path = file_path + filename
        filesize = os.stat(full_path).st_size
        #print(filename, round(filesize / 1024))
        file_info[filename] = round(filesize / 1024)
    #print(file_info)
    #context = {'file_list': os.listdir('ops_api/upload_files')}
    context = {'file_list': file_info}
    return render(request, 'www/files.html', context)

def download(request):
    file_name=request.POST.get('filename', None)
    #print(file_name)
    def file_iterator(file_name, chunk_size=512):
      with open(file_name) as f:
        while True:
          c = f.read(chunk_size)
          if c:
            yield c
          else:
            break
    file_path = 'ops_api/upload_files/'
    logging.info(file_name)
    if file_name:
       response = StreamingHttpResponse(file_iterator(file_path+file_name))
       response['Content-Type'] = 'application/octet-stream'
    # Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
       response['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name)
       return response
    else:
        return HttpResponse('未选择')