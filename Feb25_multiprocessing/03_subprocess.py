import subprocess
import threading

def intercept_output(pipe):
    for line in pipe:
        print('INTERCEPTED:', line)

args = ["python3", "serial_argv.py"]

print('DRIVER PROGRAM')

fin = open('../Mar02_from_threading_to_network/inp.txt')

pr = subprocess.Popen(args,
                      stdin=fin,
                      stdout=subprocess.PIPE,
                      stderr=None
                      )

th = threading.Thread(target=intercept_output, args=(pr.stdout, ), daemon=True)
th.start()

pr.wait()

print('SUBPROCESS IS FINISHED')

print('THE OUTPUT WAS:', pr.stdout.read())

fin.close()

print('READY')