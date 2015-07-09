from __future__ import print_function
'''
Created on 30-Apr-2014

@author: pavang
'''
import re
import os
import argparse

def rename_files(dir_path):
    file_count = 0
    if os.path.exists(dir_path):
        print("-" * 110)
        for root, dirs, files in os.walk(dir_path):    
            for filename in files:
                file_ext = filename[filename.rfind('.'):]
                new_filename = re.sub(r'[^\w]','_', filename[:filename.rfind('.')])
                os.renames(os.path.join(root, filename), os.path.join(root, new_filename + file_ext))
                print(os.path.join(root, filename) + "  -->  " + os.path.join(root, new_filename + file_ext))
                file_count = file_count + 1
        print("-" * 110)
    else:
        print("Oops! " + dir_path + ': No such directory exists')

    return file_count

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='Path of directory in which all source files are present')
    args = parser.parse_args()
    print("Done! {} files renamed ".format(rename_files(args.dir)))
    print("-" * 110)

    pass