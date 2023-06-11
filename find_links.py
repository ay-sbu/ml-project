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

print('connecting to the site... ')

torob_laptops_url = ("https://torob.com/browse/99/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%88-%D9%86%D9%88%D8%AA-%D8%A8%D9%88%DA%A9-laptop/")

offline_url = "file:///H:/torob/%D9%84%DB%8C%D8%B3%D8%AA%20%D9%82%DB%8C%D9%85%D8%AA%20%D9%84%D9%BE%20%D8%AA%D8%A7%D9%BE%20%D9%88%20%D9%86%D9%88%D8%AA%20%D8%A8%D9%88%DA%A9%D8%8C%20%DB%B2%DB%B1%20%D8%AE%D8%B1%D8%AF%D8%A7%D8%AF%D8%8C%20%D8%B5%D9%81%D8%AD%D9%87%20%DB%B4%DB%B9%20_%20%D8%AA%D8%B1%D8%A8.html"

driver.get(torob_laptops_url)

driver.execute_script('window.scrollBy(0, 2000)')
time.sleep(60)
# driver.maximize_window()

# while True:
#     page_height = driver.execute_script("return document.body.scrollHeight")
    
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait for the next set of products to load
#     print('loading...')
#     time.sleep(10)
    
#     new_page_height = driver.execute_script("return document.body.scrollHeight")

#     # Check if you've reached the end of the page
#     if new_page_height == page_height:
#         break

myelements = driver.find_elements(By.CSS_SELECTOR, ".jsx-fa8eb4b3b47a1d18 a")
print("elements len: ", len(myelements))
links_file = open('links.txt', 'w')
for i, j in enumerate(myelements):
    links_file.write(str(i) + " " + j.get_attribute('href') + "\n\n")        

print('success!')
    

    