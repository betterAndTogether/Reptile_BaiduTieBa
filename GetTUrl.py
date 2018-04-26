#coding=utf-8

import requests
import re
from bs4 import BeautifulSoup

class BDTB:

    #初始化，出入基地址，是否只看楼主参数
    def __init__(self,baseUrl,headers):

        self.baseURL =  baseUrl
        self.headers = headers

    #传入页码，获取改业帖子代码
    def getPage(self,pageNum):

        url_str = self.baseURL + '&pn=' +str(pageNum)
        session = requests.session()
        response = session.get(url_str,headers=self.headers)
        return response.text


#
def get_urls(page):

    urls = []

    #使用正则表达式
    pattern = re.compile(r'<a rel="noreferrer"  href="/p/.*</a>')
    result = pattern.findall(page)

    # print(len(result))
    # print(result)

    for a in result:

        pattern = re.compile(r'a rel="noreferrer"  href="(.*?)" title.*</a>',re.S)
        result = re.search(pattern,a)

        url_str = "http://tieba.baidu.com"+result.group(1)


        urls.append(url_str)

    return urls


def getTUrl(baseUrl,pageNum):

    # baseUrl 为贴吧贴地址
    # 参数设置
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}


    # 获取网页html
    bdtb = BDTB(baseUrl,headers)
    page = bdtb.getPage(pageNum)

    urls = get_urls(page)

    return urls


if __name__ == "__main__":

    baseUrl = "http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%B1%B1%E5%A4%A7%E5%AD%A6&ie=utf-8"
    page_num = 50
    urls = getTUrl(baseUrl,page_num)

    print(urls)

