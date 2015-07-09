from xml.dom import minidom
from bs4 import BeautifulSoup
import argparse
import zipfile as zip
import fnmatch
import os  
import shutil
import xml.etree.ElementTree as ET
"""
To Do: 
-> Total Tag Counter
-> File count
-> Summary
-> Default output directory

"""


class OoXml(object):
    """
    classify office 2k7 files with respect to specific tags and attributes

    """
    def __init__(self, src_dir_path, output_test_files_dir, target_tag, **attributes_dict):
        self.src_dir_path = src_dir_path
        self.output_test_files_dir = output_test_files_dir
        self.target_tag = target_tag 
        self.attributes_dict = attributes_dict
        self.file_tag_attr_count = 0                           # Found = Tag + Attributes with value
        self.total_tag_attr_count = 0

    def unzip_files_in_memory(self, file_path):
        self.file_tag_attr_count = 0                            # Reseting file tag counter
        zfile = zip.ZipFile(file_path, 'r')
        print '-'*20 , file_path,  '-'*20
        for name in zfile.namelist():
            if fnmatch.fnmatch(name, '*.xml'):                
                # print name
                self.parse_bs(zfile.open(name))
        if self.file_tag_attr_count:
            print "Total Count(tags & ttributes) In File: {0}".format(self.file_tag_attr_count)
        return bool(self.file_tag_attr_count)


    def parse_bs(self, _file_pointer):
        # print self.file_tag_attr_count
        xml_doc = BeautifulSoup(_file_pointer)
        # print xml_doc.findAll(True)
        tag_list = xml_doc.find_all(self.target_tag.lower()) 
        has_attributes = False

        if tag_list:
            # print tag_list[0].attrs
            count = 0
            for tag in tag_list:
                # print tag.attrs                   # Enable Attribute printing
                # print self.attributes_dict
                if all((k in tag.attrs and v == None or v == tag.attrs.get(k)) for k, v in self.attributes_dict.iteritems()):
                    # print all(tag.has_attr(attribute) == True for attribute in attributes_dict)      # Checks all attributes for truthiness
                    has_attributes = True
                    count += 1
                    # break
            # print "count", count
            print "{2} --> tag {0} found {1} times".format(self.target_tag, str(count), _file_pointer.name)
            self.file_tag_attr_count += count
            self.total_tag_attr_count += self.file_tag_attr_count
        _file_pointer.close()
        return has_attributes
      

    def controller(self):
        files_with_tag_attr = 0

        if not os.path.exists(self.output_test_files_dir):
            os.makedirs(self.output_test_files_dir)
        for _file in  os.listdir(self.src_dir_path):
            if "DS_Store" in _file:                         # Skip stupid DS_Store 
                continue
            file_path = os.path.join(self.src_dir_path, _file)
            if self.unzip_files_in_memory(file_path):
                print "copying... {0}  -->  {1} ".format(file_path, os.path.join(self.output_test_files_dir, _file))
                shutil.copy(file_path, os.path.join(self.output_test_files_dir, _file))
                files_with_tag_attr += 1

        # Summary
        print '\n\n'
        print '=' * 45, 'Summary',  '=' * 46
        print 'Total Tag Count:             {0}'.format(self.total_tag_attr_count)
        print 'Files With Tag & Attributes: {0}'.format(files_with_tag_attr)
        print 'Total Files:                 {0}'.format(len(os.listdir(self.src_dir_path)))
        print '=' * 100
        print '\n\n'

if __name__ == '__main__':
    # test_files_location = '/tmp/t/word/document.xml'
    # test_files_dir_path = '/tmp/testFiles/'
    # output_test_files_dir = '/tmp/ooxml_parsed_files'
    # target_tag = 'wp:anchor'
    # attributes = {'distl': True, 'layoutincell': True, 'relativeheight': True}

    # Parsing commandline arguments
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-input_dir_path', default = '/tmp/testFiles/', help='Test Files Directory', required=True)
    PARSER.add_argument('-output_dir_path', default = '/tmp/ooxml_parsed_files/', help='Output Test Files Directory')
    PARSER.add_argument('-tag', help='Name of the tag which you are looking for', required=True)
    PARSER.add_argument('attributes', help='Name of the tag which you are looking for', nargs='*')
    ARGS = PARSER.parse_args()
    attributes = dict()
    for item in ARGS.attributes:
        if '=' in item:
            key, value = item.split('=')
            key = key.strip().lower()
            value =value.strip()
            # print key, value
        else:
            key = item.lower()
            value = None
        attributes[key] = value

    ox = OoXml(ARGS.input_dir_path, ARGS.output_dir_path, str(ARGS.tag).strip(), **attributes)
    ox.controller()




