'''
Created on Aug 24, 2014

@author: pavang
'''
import os

def disk_usage(path):
    total = os.path.getsize(path) 
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            child_path = os.path.join(path, file_name)
            total += disk_usage(child_path)
    print('{0} --> {1}'.format(total, path))
    return total

if __name__ == '__main__':
    disk_usage('/tmp/')
    pass