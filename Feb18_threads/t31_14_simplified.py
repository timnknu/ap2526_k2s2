import os
import time
import threading

event_terminate = threading.Event()

def get_dir_contents(folder_path):
    res = {} # full_file_name -> (file_size, mtime)
    for fnm in os.listdir(folder_path):
        full_file_name = os.path.join(folder_path, fnm)
        mtime = os.path.getmtime(full_file_name)
        fsize = os.path.getsize(full_file_name)
        res[full_file_name] = (fsize, mtime)
    return res


def monitor_folder_changes(folder_path = '/tmp'):
    monitoring_interval = 5.0
    prev_snapshot = get_dir_contents(folder_path)

    while True:
        time.sleep(monitoring_interval)
        new_snapshot = get_dir_contents(folder_path)
        for full_file_name, new_file_info in new_snapshot.items():
            if full_file_name in prev_snapshot:
                old_file_info = prev_snapshot[full_file_name]
                if old_file_info != new_file_info:
                    print(f'in file {full_file_name}: contents changed')
            else:
                print(f'NEW FILE: {full_file_name}')
        #
        for full_file_name, new_file_info in prev_snapshot.items():
            if full_file_name not in new_snapshot:
                print(f'Deleted: {full_file_name}')
        #
        prev_snapshot = new_snapshot
        if event_terminate.is_set():
            print('Thread was informed that it needs to terminate!')
            break
#

th1 = threading.Thread(target=monitor_folder_changes, args=('/tmp',))
th2 = threading.Thread(target=monitor_folder_changes, args=('.',))

print('Threads created')

th1.start()
th2.start()

print('Threads started')

try:
    th1.join()
    th2.join()
except KeyboardInterrupt:
    print('Interruption via Ctrl-C detected')
    event_terminate.set()


print('Program is finished')
