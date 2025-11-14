import os
import datetime

#
print(os.listdir('folder1'))
print(os.listdir('folder2'))

folder_name = 'folder1'
for fnm in os.listdir(folder_name):
    full_name = os.path.join(folder_name, fnm)
    if os.path.isfile(full_name):
        timestamt = os.path.getctime(full_name)
        d = datetime.datetime.fromtimestamp(timestamt)
        print(fnm, os.path.getsize(full_name), d)
