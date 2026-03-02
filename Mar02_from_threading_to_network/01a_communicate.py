import subprocess
import threading

args = ["/home/tniko/tmp/MECHMAT/AP_25-26/sem2/threads/prog"]

print('DRIVER PROGRAM')

fin = open('inp.txt')

pr = subprocess.Popen(args,
                      stdin=subprocess.PIPE,
                      stdout=subprocess.PIPE,
                      stderr=None,
                      text = True
                      )
so, se = pr.communicate(input = '40000000\n',
                        timeout = 0.5)

print('so=', so)
print('se=', se)

print('SUBPROCESS IS FINISHED')
print('READY')

fin.close()

