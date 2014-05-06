from __future__ import print_function
'''
Created on 30-Apr-2014

@author: pavang
'''
import re
import os
import argparse

def rename_files(dir_path):
   if os.path.exists(dir_path):
       for filename in os.listdir(dir_path):
           if os.path.isfile(os.path.join(dir_path, filename)):
               file_ext = filename[filename.rfind('.'):]
    #          print(filename)
               new_filename = re.sub(r'[^\w]','_', filename[:filename.rfind('.')])
               os.renames(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename + file_ext))
#              print(filename)
   else:
       print(dir_path + ': No such directory exists')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='Absolute path of directory in which all source files are present')
    args = parser.parse_args()
    rename_files(args.dir)
    pass