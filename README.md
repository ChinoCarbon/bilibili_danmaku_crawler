# bilibili_danmaku_crawler
bilibili弹幕爬虫

## 项目简介
爬取指定视频的弹幕，存储到文件中

## 原理
请求弹幕api多了会被风控，但是发现b站没有管selenium爬虫，可以无限制的爬。

## 效果
自己爬b站分区top100，开了20个线程，大概是20min爬了17w条的水平。

## 快速开始
### 安装chromedriver
去https://chromedriver.chromium.org/downloads
找到符合你chrome版本的chromedriver。

如果你发现你的chrome版本比最新的还要新，就把这个json文件下载下来，找到符合你版本的chromedriver

https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json
文件我已经下载好了，放到了根目录。

### 安装依赖包

### 指定弹幕存放文件路径

### 启动文件
