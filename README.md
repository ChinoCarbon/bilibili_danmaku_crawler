# bilibili_danmaku_crawler
bilibili弹幕爬虫

## 项目简介
爬取指定视频的弹幕，存储到文件中

## 原理
请求弹幕api多了会被风控，但是发现b站没有管selenium爬虫，可以无限制的爬。

## 效果
自己爬b站分区top100，大概是20min爬了17w条的水平。

## 快速开始
### 安装chromedriver
去https://chromedriver.chromium.org/downloads
，找到符合你chrome版本的chromedriver。

如果你发现你的chrome版本比最新的还要新，就把这个json文件下载下来，找到符合你版本的chromedriver

https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json
文件我放到了根目录。

### 设置环境变量

下载好之后里面有一个叫chromedriver的可执行文件，把这个可执行文件的路径添加到环境变量。

之后打开命令行，输入chromedriver执行，有输出则为成功，大概是这样。

```
Starting ChromeDriver 120.0.6046.0 (4d5ffc8d21ca9ec585593cb5e080da0e781ef0ae-refs/branch-heads/6046@{#1}) on port 9515
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
```

### 安装依赖包
输入以下命令安装selenium爬虫。

```
npm install selenium
```

### 一些运行设置
运行前，将你需要爬取视频的cid写入cids数组。

cid获取方法：
打开一个视频，邮件检查，查看网络请求，勾上xhr，找到如下请求就能找到cid。
![image](https://github.com/ChinoCarbon/bilibili_danmaku_crawler/assets/75966357/fbfbe9d5-a86f-4753-9f2b-2bb89f3f17a6)


### 启动文件
运行main.py即可启动，可能需要等待很久才能启动。
