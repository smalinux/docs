import time
import pyautogui

from selenium import webdriver
import selenium
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Firefox()

exe_path = 'D:\python\geckodriver.exe'
binary = FirefoxBinary('C:\Program Files\Mozilla Firefox\\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary, executable_path=exe_path)

browser.get("https://soundcloud.com/smalinux")
print(selenium.__version__)

time.sleep(2)
x = browser.find_element_by_css_selector("button#onetrust-accept-btn-handler").click()
time.sleep(2)
x = browser.find_element_by_css_selector("input").send_keys("happy")
pyautogui.press('enter')
time.sleep(2)

x = browser.find_element_by_css_selector("div.soundTitle__playButton").click()
while True:
    pass
