import random
import os


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

for i in range(10):
    print(get_random_file_name())

def make_sample_directory(folder_name, r_random_files):
    if os.path.exists(folder_name):
        print('already exist', folder_name)
    else:
        os.mkdir(folder_name)
    for i in range(r_random_files):
        pass
        #with open(file_name




#make_sample_directory('folder1')

