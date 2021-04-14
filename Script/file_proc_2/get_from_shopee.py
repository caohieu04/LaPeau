import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('D:\Work\PythonEnv\chromedriver.exe')
url = 'https://shopee.vn/search?keyword=fucidin%20h'
driver.get(url)
results = []
content = driver.page_source
soup = BeautifulSoup(content)
print(soup)
#driver.quit()