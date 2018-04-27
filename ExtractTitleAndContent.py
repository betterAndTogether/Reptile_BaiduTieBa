#coding=utf-8

import requests
from bs4 import BeautifulSoup
import re

class BDTB:

    #初始化，出入基地址，是否只看楼主参数
    def __init__(self,baseUrl,seeLZ,headers):

        self.baseURL =  baseUrl
        self.seeLZ =  '?see_lz='+str(seeLZ)
        self.headers = headers
        self.page_text = None

    #传入页码，获取改业帖子代码
    def getPage(self,pageNum):

        url_str = self.baseURL +self.seeLZ + '&pn=' +str(pageNum)
        session = requests.session()
        response = session.get(url_str,headers=self.headers)
        return response.text


#根据网页page获取标题
def getTitle(bs):

    title_txt = bs.title.text
    # print(title_txt)
    return title_txt


def getContent(bs):

    content_div = bs.find_all('div',class_="d_post_content")

    # print(len(content_div))
    # exit()

    contents = []

    for div in content_div:

        contents.append(div.get_text().strip())


    return contents

def get_sum_page(page):

    '''
        <li class="l_reply_num" style="margin-left:8px"><span class="red"
        style="margin-right:3px">60</span>回复贴，共<span class="red">2</span>页</li>
    '''
    li_pattern = re.compile(r'<li class="l_reply_num".*</li>')
    li_result = li_pattern.findall(page)

    if len(li_result)==0:
        return 0
    span_pattern = re.compile(r'<span class="red">(.*?)</span>')
    result = span_pattern.findall(li_result[0])

    if len(result) == 0:
        return 0

    return result[0]


def get_title_content(baseUrl):
    '''
    :param baseUrl:具体贴的地址
    :return: title : string
            contents : str_array
    '''
    #baseUrl 为贴吧贴地址
    #参数设置
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}


    #获取网页html
    bdtb = BDTB(baseUrl,0,headers)
    page = bdtb.getPage(1)
    # print(page)

    #获取贴第一页，的title 和 第一页的content===================
    bs = BeautifulSoup(page, "html5lib")
    title = getTitle(bs)
    contents = getContent(bs)
    sum_page = get_sum_page(page)

    #============获取第一页以外其他所有的回复===================
    for i in range(int(sum_page)):

        j = i + 1
        if j == 1:
            continue

        # 获取网页html
        bdtb = BDTB(baseUrl, 0, headers)
        page = bdtb.getPage(j)

        bs = BeautifulSoup(page,"html5lib")

        contents.extend(getContent(bs))

    return title,contents

if __name__ =="__main__":

    baseUrl = "http://tieba.baidu.com/p/5536910736"
    title,contents = get_title_content(baseUrl)
    print(contents)

