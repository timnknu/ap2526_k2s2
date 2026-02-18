import os
import time

folder_path = '/tmp'
for fnm in os.listdir(folder_path):
    full_file_name = os.path.join(folder_path, fnm)
    mtime = os.path.getmtime(full_file_name)
    fsize = os.path.getsize(full_file_name)
    if fsize > 10000:
        print(full_file_name, '--', time.ctime(mtime),  fsize)