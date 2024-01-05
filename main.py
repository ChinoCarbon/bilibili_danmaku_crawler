import requests as rq
from pandas import DataFrame
import os
from os import path
import datetime as dt
import json
import time, random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
rank_api = 'https://api.bilibili.com/x/v1/dm/list.so?oid='

import mysql.connector

mydb = mysql.connector.connect(
    host="123.60.82.9",
    user="root",
    password="MyNewPass4!",
    database="visualization"
)

sql = "select cid from top_video_info"

mycursor = mydb.cursor()

mycursor.execute(sql)
res = mycursor.fetchall()

import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.common.by import By

# 设置 Chrome WebDriver 路径
#chrome_driver_path = 'C:\\Program Files\\chrome driver'

# 初始化 Chrome WebDriver
driver = webdriver.Chrome()
index = 1
for row in res:
    print("done__________________________________________________________________________" + str(index))
    file = open("../Data/danmakuData/data.txt", "a+", encoding='utf-8')
    # 访问目标网页
    driver.get('https://api.bilibili.com/x/v1/dm/list.so?oid={}'.format(row[0]))
    # 获取响应的 XML 内容
    xml_content = driver.page_source

    # 获取网页中的 <i> 标签内容
    i_tag = driver.find_elements(By.TAG_NAME, 'd')

    for den in i_tag:
        file.write(den.get_attribute('innerHTML') + '\n')
        #print(den.get_attribute('innerHTML'))
    file.close()
    index += 1
driver.quit()
