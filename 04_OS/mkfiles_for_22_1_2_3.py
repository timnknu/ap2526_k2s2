import random
import os
import time
import shutil

def get_random_file_name(n_max_file_len = 20):
    allowed_chars = ''
    for c in range(ord('0'), ord('9')+1):
        allowed_chars += chr(c)
    for c in range(ord('a'), ord('z')+1):
        allowed_chars += chr(c)
    for c in range(ord('A'), ord('Z')+1):
        allowed_chars += chr(c)
    #print(allowed_chars)
    random_len = random.randint(1, n_max_file_len)
    result = ''
    for i in range(random_len):
        j = random.randint(0, len(allowed_chars)-1)
        result += allowed_chars[j]
    return result + '.txt'

# for i in range(10):
#     print(get_random_file_name())

def make_sample_directory(folder_name, r_random_files):
    # створюємо нову папку, але лише в тому разі, якщо її ще немає
    if os.path.exists(folder_name):
        print('already exist', folder_name)
    else:
        os.mkdir(folder_name)

    # видаляємо із папки всі файли, які в ній були раніше (але саме файли, а не вкладені папки)
    for fnm in os.listdir(folder_name):
        full_name = os.path.join(folder_name, fnm)
        if os.path.isfile(full_name):
            os.remove(full_name)

    # наповнюємо папку новими файлами із випадково згенерованими іменами
    for i in range(r_random_files):
        fnm = get_random_file_name()
        full_fnm = os.path.join(folder_name, fnm)
        with open(full_fnm, 'w') as fo:
            print(f'This is my file {fnm}', file=fo)
            print('And it works great!', file=fo)
        time.sleep(1.2)
#

# make_sample_directory('folder1', r_random_files=4)
# make_sample_directory('folder2', r_random_files=4)
#print()

# Додаємо кілька файлів однакового вмісту та атриибутів (зокрема -- датою створення) у обидві папки
for i in range(1, 3):
    full_name = os.path.join('folder1', f'same_file_{i}.txt')
    with open(full_name, 'w') as fo:
        print(f'This file is the same in both folders, #{i}', file=fo)

    #time.sleep(2)
    dst = os.path.join('folder2', f'same_file_{i}.txt')
    shutil.copyfile(full_name, dst)
