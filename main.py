headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

rank_api = 'https://api.bilibili.com/x/v1/dm/list.so?oid='

###########################################数据库部分，可以自己改
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="123.60.82.9",
#     user="root",
#     password="114514",
#     database="visualization"
# )
#
# sql = "select cid from top_video_info"
# mycursor = mydb.cursor()
# mycursor.execute(sql)
# res = mycursor.fetchall()
# cids = [x[0] for x in res]
################################################

#注意这里要填入cid
cids = [1383528387, 1370621493]

from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化 Chrome WebDriver
driver = webdriver.Chrome()
index = 1
for row in cids:
    file = open("danmaku_data/data.txt", "a+", encoding='utf-8')  # 追加写入
    # 访问目标网页
    driver.get('https://api.bilibili.com/x/v1/dm/list.so?oid={}'.format(row))

    # 获取网页中的 <d> 标签内容
    i_tag = driver.find_elements(By.TAG_NAME, 'd')
    for den in i_tag:
        file.write(den.get_attribute('innerHTML') + '\n')

    file.close()
    print("done__________________________________________________________________________" + str(index))
    index += 1
driver.quit()

print("all done__________________________________________________________________________")
