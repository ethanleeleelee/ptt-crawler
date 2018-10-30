#!/usr/bin/env python
# coding: utf-8

# In[20]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

# 用 w 設定模式創立編碼
f = open(os.getcwd()+ "/data.txt",'w',encoding="utf8")

driver = webdriver.Chrome(os.getcwd() + "/chromedriver",chrome_options=options)



for i in range(1819,1821):
    driver.get("https://www.ptt.cc/bbs/NBA_Film/index" + str(i) + ".html")
    sourcecode = BeautifulSoup(driver.page_source,"html.parser")
    #print(sourcecode)
    sections = sourcecode.find_all("div","r-ent")
    for section in sections:
        sourcecode2 = BeautifulSoup(str(section),"html.parser")
        titles = sourcecode2.find_all("div","title")[0].text
        if titles.find("公告") == -1:
            print(titles)
            push = sourcecode2.find_all("div","nrec")[0].text
            print(push)
            author = sourcecode2.find_all("div","author")[0].text
            print(author)
            date = sourcecode2.find_all("div","date")[0].text
            print(date)
            data = titles + "\n" + push + "\n" + author + "\n" + date
            f.write(data)

driver.quit()


f.close()
    


# In[ ]:


#更換字串
str.replace("bla","bluuuuu")
#去掉字串中空格
str.stip()
#檢查字串首字串尾
str.startswith("bla"),str.endswith("bla")


# In[ ]:




