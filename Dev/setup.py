'''
creating package(.gz) in dist directory
	python setup.py sdist
 
Created on Aug 21, 2014
==4.3.2

@author: pavang
'''
from distutils.core import setup
# 
# setup(
#       name = 'synutil',
#       version = '1.1.0',
#       py_modules = ['fix_file_name'],
#       install_requires = ['beautifulsoup4==4.3.2'],
#       setup_requires = ['beautifulsoup4==4.3.2'],
#       author = 'Pavan Gupta',
#       author_email = 'pavan.gupta@synerzip.com',
#       description = 'removes special charecters from file name'      
#       )

setup(
      name = 'synutil',
      version = '1.3',
      py_modules = ['fix_files_name', 'prop_parser', 'download_build', 'md5_unique'],
      install_requires = ['beautifulsoup4==4.3.2'],
      setup_requires = ['beautifulsoup4==4.3.2'],
      author = 'Pavan Gupta',
      author_email = 'pavan.gupta@synerzip.com',
      description = 'updated download_build script for downloading release build'      
      )
