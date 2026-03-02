import subprocess
import threading

def intercept_output(pipe):
    for line in pipe:
        print('INTERCEPTED:', line)

args = ["/home/tniko/tmp/MECHMAT/AP_25-26/sem2/threads/prog"]

print('DRIVER PROGRAM')

fin = open('inp.txt')

pr = subprocess.Popen(args,
                      stdin=fin,
                      stdout=subprocess.PIPE,
                      stderr=None,
                      text = True
                      )
th = threading.Thread(target=intercept_output, args=(pr.stdout, ), daemon=True)
th.start()

process_finished_successfully = False

try:
    pr.wait(timeout=3.5)
    process_finished_successfully = True
except subprocess.TimeoutExpired:
    print('TIMEOUT')
    pr.terminate()
    # process_finished_successfully = False

if process_finished_successfully:
    print('SUBPROCESS IS FINISHED')
    print('THE OUTPUT WAS:', pr.stdout.read())
    print('READY')
else:
    print('PROCES  TERMINATED')

fin.close()

