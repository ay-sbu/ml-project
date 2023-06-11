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

links_file = open('links.txt', 'r')
links_str = links_file.read()

links = links_str.split('\n\n')

# for i in range(10):
# 	print(i)
# 	print(links[i])

print("len(links)", len(links))

distinct_titles = {}

for i in range(len(links)):
	driver.get(links[i])

	titles = driver.find_elements(By.CSS_SELECTOR, ".jsx-5b5c456cc255c2dc.detail-title")

	print("len(titles)", len(titles))
	for i in range(len(titles)):
		distinct_titles.add(titles[i].get_attribute("innerHTML"))

print(len(distinct_titles))