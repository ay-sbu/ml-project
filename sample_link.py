import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.chrome.options import Options
import os

os.environ['PATH'] += r"C:/SeleniumDrivers"

chrome_options = Options()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

first_link = "https://torob.com/p/c9e081d5-cc85-4cd5-98d3-116aa2b9aba2/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%84%D9%86%D9%88%D9%88-ideapad-3-4gb-ram-1tb-hdd-n4020-hd/"
driver.get(first_link)

titles = driver.find_elements(By.CSS_SELECTOR, ".jsx-5b5c456cc255c2dc.detail-title")
values = driver.find_elements(By.CSS_SELECTOR, ".jsx-5b5c456cc255c2dc.detail-value")

print("len(titles)", len(titles))
for i in range(len(titles)):
	print(titles[i].get_attribute("innerHTML"))
	print(values[i].get_attribute("innerHTML"))