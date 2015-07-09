'''
Created on 04-Sep-2013

@author: pavang
'''
import os

class RenameFiles(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def rnFiles(self, path):
        list = os.listdir("/private/tmp/RoundTrip/")
        for filename in list:
            firstPart = filename[:filename.index('.')]
            secondPart = filename[filename.index('.'): ]
            os.rename(filename, firstPart + "_rt" + secondPart)
        
        
#         for filename in os.listdir("."):
# ...  if filename.startswith("cheese_"):
# ...    os.rename(filename, filename[7:])
#         