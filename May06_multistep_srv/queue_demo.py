import threading
import queue
import time

q_main_to_th = queue.Queue()
q_th2main = queue.Queue()

def worker():
    print('Thread started')
    item = q_main_to_th.get()
    print('Thread received', item)
    time.sleep(4)
    q_th2main.put(item ** 2)
    print('Thread finished')
    q_main_to_th.task_done()

print('Main program started')
time.sleep(4)
# Turn-on the worker thread.
th = threading.Thread(target=worker, daemon=True)
th.start()
time.sleep(1)
print('Main program send data to the thread')
q_main_to_th.put(15)
print('Awaiting result from the thread')
print('Result:', q_th2main.get())

# Block until all tasks are done.
q_main_to_th.join()
print('All work completed')