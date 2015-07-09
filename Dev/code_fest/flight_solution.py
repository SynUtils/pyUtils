'''
Created on 14-Mar-2014

@author: pavang
'''

from selenium import webdriver
firefox_driver = None

def search_flight():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get("http://www.ixigo.com")
    firefox_driver.implicitly_wait(5)
    firefox_driver.find_element_by_id("homeListItemFlights").click()
    firefox_driver.find_element_by_id("originCityInput").send_keys("Mumbai, India - Chatrapati Shivaji International Airport(BOM)")
    firefox_driver.find_element_by_id("destCityInput").send_keys("New Delhi, India - Indira Gandhi Intl Airport(DEL)")   
    firefox_driver.find_element_by_xpath("html/body/div[2]/div[3]/div[1]/div[2]/div/div/div/div[4]/div[3]/div[2]/form/div[1]/div/div[2]/div[1]/div/span").click() 
    firefox_driver.find_element_by_id("30/03/2014").click()                                                           
    firefox_driver.find_element_by_id("actionSearch").click()


if __name__ == "__main__":
    search_flight()
  