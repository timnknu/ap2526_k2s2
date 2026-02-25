import subprocess

args = ["python3", "serial_argv.py"]

print('DRIVER PROGRAM')

fin = open('inp.txt')

pr = subprocess.Popen(args,
                      stdin=fin,
                      stdout=None,
                      stderr=None
                      )

pr.wait()


fin.close()

print('READY')