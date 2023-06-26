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
# driver.maximize_window()

print('connecting to the site... ')

torob_laptops_url = ("https://torob.com/browse/99/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%88-%D9%86%D9%88%D8%AA-%D8%A8%D9%88%DA%A9-laptop/")

driver.get(torob_laptops_url)

time.sleep(60)

myelements = driver.find_elements(By.CSS_SELECTOR, ".jsx-fa8eb4b3b47a1d18 a")
print("elements len: ", len(myelements))
links_file = open('links.txt', 'w')
for i, j in enumerate(myelements):
    links_file.write(str(i) + " " + j.get_attribute('href') + "\n\n")        

print('success!')
    

    