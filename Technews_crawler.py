#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(os.getcwd() + "/chromedriver.exe",chrome_options = options)

for i in range(1, 2):
    driver.get("https://technews.tw/category/internet/page/" + str(i))
    time.sleep(0.5)
    sourcecode = BeautifulSoup(driver.page_source, "html.parser")
    contents = sourcecode.find_all("div","content")
    for content in contents:
        sourcecode2 = BeautifulSoup(str(content), "html.parser")
        titles = sourcecode2.find_all("h1","entry-title")
        print(titles[0].string)
        sourcecode3 = BeautifulSoup(str(titles), "html.parser")
        a = sourcecode3.find_all("a")
        for i in a:
            print(i.get("href"))
        minfs = sourcecode2.find_all("div","moreinf")[0].text
        print(minfs)
driver.quit()

