'''
Created on Nov 6, 2014

@author: pavang
'''

from PIL import Image
import os

def crop_images(source_images_dir, width, height):

    for root, dirs, files in os.walk(source_images_dir):    
            for filename in files:
                if 'DS_Store' in filename:
                    continue
                if source_images_dir[-1] == '/':
                    new_root = source_images_dir.split('/')[-2]
                else:
                    new_root = source_images_dir.split('/')[-1]
                destination_images_dir_path =  source_images_dir[:source_images_dir.rfind(new_root)] + 'crop_' + new_root + root[len(source_images_dir) - 1:]
                if not os.path.exists(destination_images_dir_path):
                    os.makedirs(destination_images_dir_path)
                file_path = os.path.join(root, filename)
#                 print os.path.join(destination_images_dir, filename)
                crop_image(file_path, os.path.join(destination_images_dir_path, filename), width, height)
    pass

def crop_image(source_img_path, destination_img_path, width, height):
    img = Image.open(source_img_path)
    x,y = img.size
    color = (255, 255, 255, 0)                     #White color
    img.crop((0, 0, width, height)).save(destination_img_path)
    cropped_img = Image.open(destination_img_path)
    crop_x, crop_y = cropped_img.size
    print source_img_path, x, str(y) +'   -->  '+ destination_img_path, crop_x, crop_y

    if x >= crop_x and y >= crop_y:
        pass
    else:
        fill_color(destination_img_path, color, x-1, 0, crop_x, crop_y)
        fill_color(destination_img_path, color, 0, y, crop_x, crop_y)

    print '-' * 150
#     pass

def fill_color(src_img, color, start_widht, start_height, end_width, end_height):
    box1 = (start_widht, start_height, end_width, end_height)
    target_img = Image.open(src_img)    
    target_img.paste(color, box = box1)
    target_img.save(src_img, 'PNG')
    # print target_img.size
    pass   


if __name__ == '__main__':
    source_images_path = ["/tmp/MSO_XLSX/", "/tmp/GDocs_XLSX/",  "/tmp/Office365_xlsx/",  "/tmp/QOC_xlsx/", "/tmp/iWORK_XLSX/"]
    
    width = 1920
    height = 788
    
    for i in range(len(source_images_path)):
        crop_images(source_images_path[i], width, height)
    # color = (255, 255, 255, 0)                     #White color
    # fill_color('/tmp/crop1.png', color, 1649, 0, 1920, 788)
    pass


