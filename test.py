from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
cwd = os.getcwd()

driver = webdriver.Firefox()
driver.get(f"http://o4ugdf54plqu.github.io/")
blog_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Blog')
blog_link.click()
links = driver.find_elements(By.TAG_NAME, "a")
urls = []
for link in links:
    urls.append(link.get_attribute("href"))

for url in urls:
    driver.get(url)
    print(driver.title)
    assert "404" not in driver.page_source
time.sleep(5)
driver.close()