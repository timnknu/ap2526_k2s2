import subprocess

args = ["python3", "serial_argv.py"]

print('DRIVER PROGRAM')

fin = open('inp.txt')

pr = subprocess.Popen(args,
                      stdin=fin,
                      stdout=subprocess.PIPE,
                      stderr=None
                      )

pr.wait()

print('SUBPROCESS IS FINISHED')

print('THE OUTPUT WAS:', pr.stdout.read())

fin.close()

print('READY')