# app.py
# Arie M. Prasetyo, 210920

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_argument("--headless")

# EXE_PATH = r'./chromedriver'
EXE_PATH = r'./chromedriver_mac' # when testing in non-Docker
driver = webdriver.Chrome(executable_path=EXE_PATH, options=chrome_options)

# open the site
driver.get("https://app.astrnt.co")

print(driver.title)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.save_screenshot('screens/1.png')

# close driver
driver.close()