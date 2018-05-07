# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:01:04 2018

@author: Prometheus
"""
# Automating Shaing request with 23andme

#Importing libraries
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# login

driver = webdriver.Chrome()
driver.get('https://you.23andme.com/tools/relatives/#people?sort=not_sharing_first')
wait = WebDriverWait(driver, 1)
# Enter email
elem = driver.find_element_by_id('email')
elem.send_keys("your@email.com")
# Select password field and enter yours
elem = driver.find_element_by_id('password')
elem.send_keys("yourpassword")
elem.send_keys(Keys.RETURN)

# Go to correct URL
driver.get('https://you.23andme.com/tools/relatives/#people?sort=not_sharing_first')

        
# Load URl and count list of relatives           



try:  
    for i in range (0,1200):
        # Let website load before clicking on relative
        time.sleep(2)
        # Select and click on Relative from list
        driver.find_element_by_xpath(".//*[contains(@class, 't-row t-row--body')]").click()
        # Click on "Share Reports"
        driver.find_element_by_class_name('js-share').click()
        # Go back to list on previous page
        driver.back()     
    
except NoSuchElementException:
    print('NoSuchElementExceptionEncountered')
    
else:
    print('Done')

driver.quit()
    

