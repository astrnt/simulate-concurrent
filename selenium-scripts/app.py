# app.py
# Arie M. Prasetyo, 210920

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

# local
# EXE_PATH = r'./chromedriver' # when testing in non-Docker (linux)
# EXE_PATH = r'./chromedriver_mac' # when testing in non-Docker (macos)
# driver = webdriver.Chrome(executable_path=EXE_PATH, options=chrome_options)

# docker (remote)
#driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME, options=chrome_options)
# driver = webdriver.Remote( command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
driver = webdriver.Remote( command_executor='http://192.168.43.172:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME, options=chrome_options)

# open the site
driver.get("https://app.astrnt.co")

print(driver.title)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.save_screenshot('screens/1.png')

# close driver
driver.close()