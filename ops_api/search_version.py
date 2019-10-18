from kubernetes import client, config

import os

file_path='upload_files/'
c=os.listdir(file_path)
print(c)
for i in c:
#    print(i)
    full_path=file_path+i
    aa=os.stat(full_path).st_size
    print(i,round(aa/1024))