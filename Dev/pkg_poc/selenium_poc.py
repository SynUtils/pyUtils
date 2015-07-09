'''
Created on 17-Feb-2014

@author: pavang
'''
firefox_driver = None

def write_details(uidai):
    global firefox_driver
    firefox_driver.find_element_by_id('cert_no').send_keys(uidai)
    firefox_driver.find_element_by_xpath("//*[@id='reg_frm']/table/tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[5]/input").click()
    # Xpath pattern of Field
#     .//*[@id='maincont']/center/table[2]/tbody/tr[2]/td[2]/b
#     .//*[@id='maincont']/center/table[2]/tbody/tr[3]/td[2]/b
#     .//*[@id='maincont']/center/table[2]/tbody/tr[4]/td[2]/b
#     ..
#     ..
#     .//*[@id='maincont']/center/table[2]/tbody/tr[19]/td[2]/b

    # Xpath pattern of Value
#     .//*[@id='maincont']/center/table[2]/tbody/tr[2]/td[4]
#     ..
#     ..   
#     .//*[@id='maincont']/center/table[2]/tbody/tr[19]/td[4]

    print '-' * 40 + uidai + '-' * 40
    with open('/tmp/' + uidai +'.txt','w') as out_file:
        for i in range(2, 20):
            field = firefox_driver.find_element_by_xpath("//*[@id='maincont']/center/table[2]/tbody/tr[" + str(i) + "]/td[2]/b").text
            value = firefox_driver.find_element_by_xpath("//*[@id='maincont']/center/table[2]/tbody/tr[" + str(i) + "]/td[4]").text
            print field, value
            out_file.write(field + ":" + value + '\n')         
    

if __name__ == '__main__':
    from selenium import webdriver
    firefox_driver = webdriver.Firefox()
    input_list = ['SO147629', 'SO147616']
    
    for item in input_list:
        firefox_driver.get("http://uidai.sifyitest.com/cert_search.php")
        write_details(item)        
                
    firefox_driver.quit()
