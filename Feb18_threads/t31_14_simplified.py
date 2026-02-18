import os
import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG)

event_terminate = threading.Event()
event_thread_failed = threading.Event()

def get_dir_contents(folder_path):
    res = {} # full_file_name -> (file_size, mtime)
    for fnm in os.listdir(folder_path):
        full_file_name = os.path.join(folder_path, fnm)
        mtime = os.path.getmtime(full_file_name)
        fsize = os.path.getsize(full_file_name)
        res[full_file_name] = (fsize, mtime)
    return res

class MyMonitoringThread(threading.Thread):
    def __init__(self, folder_path):
        self._folder_path = folder_path
        super().__init__()

    def monitor_folder_changes(self):
        folder_path = self._folder_path
        monitoring_interval = 1.0
        prev_snapshot = get_dir_contents(folder_path)

        while True:
            if event_thread_failed.is_set():
                break

            if event_terminate.wait(monitoring_interval):
                logging.debug('Thread was informed that it needs to terminate!')
                break
            else:
                logging.debug(' .wait() returned false')

            if folder_path=='/tmp':
                1/0

            new_snapshot = get_dir_contents(folder_path)
            for full_file_name, new_file_info in new_snapshot.items():
                if full_file_name in prev_snapshot:
                    old_file_info = prev_snapshot[full_file_name]
                    if old_file_info != new_file_info:
                        logging.info(f'in file {full_file_name}: contents changed')
                else:
                    logging.info(f'NEW FILE: {full_file_name}')
            #
            for full_file_name, new_file_info in prev_snapshot.items():
                if full_file_name not in new_snapshot:
                    logging.info(f'Deleted: {full_file_name}')
            #
            prev_snapshot = new_snapshot
    #
    def run(self):
        try:
            self.monitor_folder_changes()
        except:
            print('В ПОТОЦІ СТАЛАСЯ ПОМИЛКА!!!!!!!!!!!!!')
            event_thread_failed.set()


th1 = MyMonitoringThread('/tmp')
th2 = MyMonitoringThread('.')


logging.debug('Threads created')

th1.start()
th2.start()

logging.debug('Threads started')

try:
    th1.join()
    th2.join()
except KeyboardInterrupt:
    logging.info('Interruption via Ctrl-C detected')
    event_terminate.set()

if event_thread_failed.is_set():
    logging.info('Програма завершуєтсья аварійно, бо аварійно завершився один із її потоків, а в цій програмі не було передбачено, як дійся в такому випадку! Караул!!!')

logging.info('Program is finished')
