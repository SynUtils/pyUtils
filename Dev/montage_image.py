import os.path
import sys
from time import strftime
import Image

row_size = 4
margin = 3

def generate_montage(filenames, output_fn):
    images = [Image.open(filename) for filename in filenames]
    print filename
    width = max(image.size[0] + margin for image in images)*row_size
    height = sum(image.size[1] + margin for image in images)
    montage = Image.new(mode='RGBA', size=(width, height), color=(0,0,0,0))

    max_x = 0
    max_y = 0
    offset_x = 0
    offset_y = 0
    for i,image in enumerate(images):
        montage.paste(image, (offset_x, offset_y))

        max_x = max(max_x, offset_x + image.size[0])
        max_y = max(max_y, offset_y + image.size[1])

        if i % row_size == row_size-1:
            offset_y = max_y + margin
            offset_x = 0
        else:
            offset_x += margin + image.size[0]

    montage = montage.crop((0, 0, max_x, max_y))
    montage.save(output_fn)
    
def get_files_list(directory_path):
    file_list = []
    for root, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            file_list.append(filename)

def get_common_files(*dirs):
    print dirs
    intersected_set = set()
    for i,directory in enumerate(dirs[0]):
        if not i:
            intersected_set = set(os.listdir(directory))
#         print(directory)
#         print(os.listdir(directory))
        else:
            intersected_set = intersected_set.intersection(set(os.listdir(directory)))
    return list(intersected_set)

def get_path_list(files_list, *dirs):
    files_dict = {}
    for _file in files_list:
        files_dict[_file] = []
        for directory in dirs[0]:
            files_dict[_file].append(os.path.join(directory, _file))
    return files_dict




if __name__ == '__main__':
#     basename = strftime("Montage %Y-%m-%d at %H.%M.%S.png")
#     exedir = os.path.dirname(os.path.abspath(sys.argv[0]))
#     filename = os.path.join(exedir, basename)
#     #33print sys.argv[1:3]
#     print sys.argv[1:]
#     files_list = get_common_files(sys.argv[1:])
#     path_dict = get_path_list(files_list, sys.argv[1:])
#     for key,  value in path_dict.items():
#         generate_montage(value, filename)

    #pathlist = for path in files_list
    print "running Montage image"
    pass


    