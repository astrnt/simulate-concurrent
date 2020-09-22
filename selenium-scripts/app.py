# app.py
# Arie M. Prasetyo, 210920

import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

machine_ip = '192.168.43.172'
remote_executor = 'http://' + machine_ip + ':4444/wd/hub'
target_site = 'https://astrnt.co/'

# set up driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
driver = webdriver.Remote(command_executor=remote_executor, desired_capabilities=DesiredCapabilities.CHROME, options=chrome_options)

# open the site
driver.get(target_site)

# get information of homepage
print(driver.title)
print(driver.current_url)

# go to regisration page
elem_try = driver.find_element_by_class_name('try')
elem_try.click()
time.sleep(.5)

# get information of registration page
print(driver.title)
print(driver.current_url)

# get screenshot of the bottom part of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.save_screenshot('screens/1.png')

# close driver
driver.close()