#codin=utf-8
import requests
import json

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
cookie = {}
session = requests.session()

# 要爬取的网页地址列表(按时间排序的话题榜单以及按热点事件排序的话题榜单)
urllist = ["https://www.zhihu.com/topic/19608566/newest", "https://www.zhihu.com/topic/19608566/hot"]
response = session.get("https://www.zhihu.com/topic/19608566/hot", headers=headers)

print(response.text)


