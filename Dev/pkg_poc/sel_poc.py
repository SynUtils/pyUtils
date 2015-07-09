#!/usr/bin/python
'''
Created on 17-Feb-2014

@author: pavang
'''

import subprocess
import os
import urllib

if __name__ == '__main__':
    from selenium import webdriver
    firefox_driver = webdriver.Firefox()
    firefox_driver.get("http://www.occ.gov/static/interpretations-and-precedents/aug01/intaug01.html")
    
    links =     firefox_driver.find_elements_by_tag_name('a')
    
    with open('/tmp/output.txt','w') as out_file:     
        for link in links:
            print(link.text +'   -->   '+ str(link.get_attribute('href')))
            out_file.write(link.text +'   ,   '+ str(link.get_attribute('href')) + '\n')
#             urllib.request.urlretrieve(str(link.get_attribute('href')))

#     print(os.path.curdir)
#     print(os.getcwd())
#     subprocess.call(['wget','http://www.occ.gov/static/interpretations-and-precedents/aug01/int912.pdf'])       
#     os.system(r"wget http://www.occ.gov/static/interpretations-and-precedents/aug01/int912.pdf")
#     urllib.request.urlretrieve("http://www.occ.gov/static/interpretations-and-precedents/aug01/int912.pdf")
                 
    firefox_driver.quit()
