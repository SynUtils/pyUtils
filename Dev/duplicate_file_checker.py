'''
Created on Sep 23, 2014

@author: pavang
'''
import os
def get_common_files(*dirs):
#     print(dirs)
    intersected_set = set()
    for i,directory in enumerate(dirs[0]):
        if not i:
            intersected_set = set(os.listdir(directory))
#         print(directory)
#         print(os.listdir(directory))
        else:
            intersected_set = intersected_set.intersection(set(os.listdir(directory)))
    return intersected_set

def get_path_list(files_list, *dirs):
    files_dict = {}
    for _file in files_list:
        files_dict[_file] = []
        for directory in dirs[0]:
            files_dict[_file].append(os.path.join(directory, _file))
    return files_dict
            
if __name__ == '__main__':
    ms_files = '/tmp/ms'
    qo_files = '/tmp/qo'
    gdrive_files = '/tmp/gdrive'
    iworks_files = '/tmp/iworks'
    files_list = get_common_files([ms_files, qo_files, gdrive_files, iworks_files])
    files_path_dict = get_path_list(files_list, [ms_files, qo_files, gdrive_files, iworks_files])
        
#     print(files_list)
    
    pass