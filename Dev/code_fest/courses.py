#!/usr/bin/python
'''
Created on 17-Feb-2014

@author: pavang
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


properties = {}
object_repo = {}
firefox_driver = None

def fill_property():
    global properties
    with open('/Users/pavang/Documents/IDE Projects/workspace/py_poc/src/code_fest/propeties.txt','r') as prop:
        for line in prop.readlines():
            key, value = line.split('=')
            properties[key] = value

def fill_object_repo():
    global object_repo
    with open('/Users/pavang/Documents/IDE Projects/workspace/py_poc/src/code_fest/object_repo.txt','r') as obj_repo:
        for line in obj_repo.readlines():
            key, value = line.split('=')
            object_repo[key] = value
        

def print_dict(dict_data, separator='='):
    """
        print given dictionary and put separator between key and value
        while printing
    """
    for key, value in dict_data.items():
        print(str(key) + separator + '   ' + str(value))

def do_login():
    global firefox_driver
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(" http://enterprise.demo.orangehrmlive.com/")
#     firefox_driver.implicitly_wait(5)
    firefox_driver.find_element_by_id(str(object_repo["user_id"]).strip()).send_keys(str(properties["user_id"]).strip())
    firefox_driver.find_element_by_id(object_repo["password"].strip()).send_keys(properties["password"].strip())
#     firefox_driver.implicitly_wait(10)
    firefox_driver.find_element_by_id(object_repo["login_button"].strip()).click()
    
def hover():
    global firefox_driver
    training_tab = firefox_driver.find_element_by_xpath(object_repo["training_tab"].strip())
    #Training
    hov = ActionChains(firefox_driver).move_to_element(training_tab)
    hov.perform()
    firefox_driver.find_element_by_xpath(object_repo["courses"].strip()).click()

def count_courses_list():
    global firefox_driver
    table = firefox_driver.find_element_by_id(object_repo["courses_table"].strip())
    courses_count = table.find_elements_by_tag_name('tr')
#     for i, row in enumerate(courses_count)
    return (len(list(courses_count))-1)
    

    
def add_course():
    global firefox_driver
    firefox_driver.find_element_by_id(object_repo["add_course_button"].strip()).click()
    firefox_driver.find_element_by_id(object_repo["add_course_title"].strip()).send_keys(properties["title"].strip())
    firefox_driver.find_element_by_id(object_repo["add_course_coordinator"].strip()).send_keys(properties["coordinator"].strip())
    firefox_driver.find_element_by_id(object_repo["add_course_save_button"].strip()).click()
    
def delete_course():
    global firefox_driver
    firefox_driver.find_element_by_id("ohrmList_chkSelectRecord_5").click()
    firefox_driver.find_element_by_id("btnDelete").click()
    firefox_driver.switch_to_active_element()
    firefox_driver.find_element_by_id("dialogDeleteBtn").click()
    

def search_course():
    global firefox_driver
    firefox_driver.find_element_by_id("searchCourse_title").send_keys("AWS Training")
    firefox_driver.find_element_by_id("searchCourse_coordinator_empName").send_keys("Jacqueline White")
    firefox_driver.find_element_by_id("searchBtn").click() 
    
if __name__=='__main__':
    fill_property()
    fill_object_repo()
    print('=' * 30 + '   properties file   ' + '=' * 40)
    print_dict(properties)
    
    
    print('=' * 30 + '   object repo   ' + '=' * 40)
    print_dict(object_repo)

    do_login()
    hover()
    
    print('=' * 30 + '   No Of Courses   ' + '=' * 40)
    
    print(count_courses_list())
   
    delete_course()
    search_course()
    add_course() 



                 
    
