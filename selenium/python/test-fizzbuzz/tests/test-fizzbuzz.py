#! /usr/local/bin/python3 

# This is a Selenium WebDriver test
#
# Attempt to test my FizzBuzz HTML - CSS - Javascript project 
#
# Written by: Stephen Jonker
# Written on: Tueday 20 Feb 2018
#
# Purpose:
# - This is a basic introduction into Selenium.
# - Attempt to automate the HTML - CSS - FizzBuzz web page I did recently 
# - Use Python - Selenium WebDriver - Firefox
#
# - It basically seems to work.  Really basic though 

import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(log_path='./logs/geckodriver.log')
#
# CHANGE FULL PATH TO index.html IN LINE BELOW TO SUITE YOUR DIRECTORY STRUCTURE
#
browser.get('file:///Users/sjonker/devx/selenium-python-sample-code/fizzbizz-test/index.html')

# Ya, good to this point, the Firefox browser launches and loads the correct page from the 
# filesystem.  Note: three forward slashes after the file: is key

#assert 'xxxFizzBuzz Javascript Example' in browser.title
assert 'FizzBuzz Javascript Example' in browser.title

# Ya, the above assertion also appears to work, or fail, depending on which one you use

browser.save_screenshot('./screenshots/foo123.png')

elem = browser.find_element_by_id('AUT-button-doFizzBuzz')  # Find the button
elem.click()

# Pause the python script for 5 seconds to observe the output of the script
# Ya, in the future, test will be written to verify the output.  But this is a basic script for now.
#
time.sleep(5)

# Ok, added an ID to the button element on the HTML FizzBuzz web page
# Found the button by_ID 
# Executed a button click and the javascript attached to the onClick event ran
# FizzBuzz output was seen on the webpage in the output area. All done via Python. 
# No real testing at this point, but we are driving a web page with Python code.
# Very cool

# Clean up the browser, we are done.
browser.quit()

# EOF
