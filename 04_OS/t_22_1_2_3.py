import os
import datetime

def get_files_info(folder_name):
    result = {}
    for fnm in os.listdir(folder_name):
        full_name = os.path.join(folder_name, fnm)
        if os.path.isfile(full_name):
            timestamt = os.path.getctime(full_name)
            d = datetime.datetime.fromtimestamp(timestamt)
            #print(fnm, os.path.getsize(full_name), d)
            result[fnm] = (os.path.getsize(full_name), d)
    return result

info1 = get_files_info('folder1')
info2 = get_files_info('folder2')

files_uniq_to_folder1 = []
for k1, v1 in info1.items():
    if k1 not in info2:
        files_uniq_to_folder1.append(k1)#(k1, v1))

files_uniq_to_folder2 = []
for k2, v2 in info2.items():
    if k2 not in info1:
        files_uniq_to_folder2.append(k2)#(k2, v2))

print("Файли лише в папці №1:", files_uniq_to_folder1)
print("Файли лише в папці №2:", files_uniq_to_folder2)

for k1, v1 in info1.items():
    if k1 in info2:
        print(f'FILE {k1} IS IN BOTH DIRECTORIES')
        print("In folder1:", v1[1])
        print("In folder1:", info2[k1][1])
        d1 = v1[1]
        d2 = info2[k1][1]
        time_difference = d1 - d2 if d1>=d2 else d2 - d1
        print('time difference:', time_difference)
        if d1 > d2:
            print(k1, 'is newer')
        elif d2 > d1:
            print(k2, 'is newer')
        else:
            print(k1, 'has the same date as', k2)
        #
        size1 = v1[0]
        size2 = info2[k1][0]
        print('|difference in sizes|:', abs(size1 - size2))
        print('-'*80)
    else:
        pass

