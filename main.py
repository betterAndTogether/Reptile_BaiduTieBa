#coding=utf-8

import re
import ExtractTitleAndContent
import GetTUrl
import os


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


    #获取贴吧基地址
def get_TBBaseUrls():

    TBBaseUrl = []
    sca_page_num = []

    with open("./TBUrl.txt",'r',encoding="utf-8") as  f:

        line = f.readline()

        while line:

            line_arr = line.strip().split(',')

            TBBaseUrl.append(line_arr[0])
            sca_page_num.append(int(line_arr[1]))

            line = f.readline()

    return TBBaseUrl,sca_page_num


def main():

    TBBaseUrls,sca_page_num = get_TBBaseUrls()

    for i in range(len(TBBaseUrls)):

        TbaseUrls = []

        for j in range(sca_page_num[i]):

            #获取该贴吧的所有贴的地址
            page_num = j * 50
            TbaseUrls.extend(GetTUrl.getTUrl(TBBaseUrls[i],page_num))


        #生成一个贴吧的文件夹
        path = "./Data/"+str(i)
        mkdir(path)

        #根据每个贴，获取器title,和contents
        for TbaseUrl in TbaseUrls:

            title,contents = ExtractTitleAndContent.get_title_content(TbaseUrl)

            pattern = re.compile(r'\W')

            title = re.sub(pattern, '', title)
            print(title)

            if len(title) > 20:
                title = title[0:20]

            #写入文件
            with open("{}/{}.txt".format(path,title),'w',encoding='utf-8') as wf:

                wf.write(title+"\n")

                for content in contents:

                    wf.write(content)
                    wf.write('\n')



if __name__ == "__main__":

    main()

