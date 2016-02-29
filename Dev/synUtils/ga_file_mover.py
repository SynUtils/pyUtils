from __future__ import print_function
'''
Created on Jul 16, 2014

@author: pavang
'''
import os
import shutil

def move(src_dir_path, dest_dir_path, files_to_be_moved):
    src_dir = os.listdir(path = src_dir_path)
    input_list = [_file[:-1] for _file in open(files_to_be_moved)]
    for file_name in src_dir:
        if file_name in input_list:
            full_file_name = os.path.join(src_dir_path, file_name)
            if(os.path.isfile(full_file_name)):
                shutil.copy(full_file_name, dest_dir_path)
            print(file_name)
        pass
        
        
if __name__ == '__main__':
    src_dir_path = '/private/tmp/1'
    dest_dir_path = '/private/tmp/2'
    files_to_be_moved = '/private/tmp/input'
    move(src_dir_path, dest_dir_path, files_to_be_moved)
    pass