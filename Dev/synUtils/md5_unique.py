'''
Created on Nov 10, 2014

@author: pavang
'''
import os
import subprocess
import hashlib
import shutil
md5_data = {}
 
def get_unique_md5_data(source_dir_path):
    global md5_data
    for root, dirs, files in os.walk(source_dir_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            output = subprocess.Popen(['md5', file_path],stdout=subprocess.PIPE)
            for line in iter(output.stdout.readline, ''):
#                 print line
                new_line = str(line).replace('MD5 (', '').replace(') =', '')
#                 print new_line
                value, key = new_line.split(' ')
                md5_data[key] = value
                
#             data = file_path.read() 
#             print hashlib.md5(file_path).hexdigest()
    print '-' * 100
#     print md5_data

def move_unique(destination_dir_path):
    for k, v in md5_data.items():
        print k +'   -->  '+ v

#         shutil.copyfile(v, destination_dir_path)


if __name__ == '__main__':
    get_unique_md5_data('/tmp/DailyRun')
    move_unique('/tmp/unique/')
    pass




