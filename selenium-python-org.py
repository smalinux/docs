import time
import pyautogui
from selenium import webdriver
import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

#
browser = webdriver.Firefox()
exe_path = 'D:\python\geckodriver.exe'
binary = FirefoxBinary('C:\Program Files\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary, executable_path=exe_path)
#

browser.get("https://www.python.org/")
assert "Python" in browser.title

elem = browser.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(3)
scroll = browser.find_element_by_tag_name("body")
scroll.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
scroll.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
scroll.send_keys(Keys.PAGE_DOWN)

# elem.send_keys(Keys.PAGE_DOWN)
assert "No results found." not in browser.page_source

# browser.save_screenshot('screenshot.png')

time.sleep(3)
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


while True:
    pass
