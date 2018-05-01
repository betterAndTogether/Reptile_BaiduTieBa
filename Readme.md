#
    Topic:爬取百度贴吧
#

#文件简介#

#GetTUrl.py

    ##根据具体的贴吧，提取贴吧所有的贴的地址： urls <address array>

    Example:

        baseUrl = "http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%B1%B1%E5%A4%A7%E5%AD%A6&ie=utf-8"
        page_num = 50
        urls = getTUrl(baseUrl,page_num)
        print(urls)

#ExtractTitleAndContent.py

    ## 爬取具体某个贴的标题：title  和 所有评论数据：content <string array>

    Example:

        baseUrl = "http://tieba.baidu.com/p/5536910736"
        title,contents = get_title_content(baseUrl)
        print(contents)

#main.py

    ##读取txt文件TBUrl.txt中的贴吧的地址，和 爬出贴吧的网页个数
    ##组织以上两个py文件，进行自动爬取贴百度贴吧

    #输出
        建立文件夹 ./Data





