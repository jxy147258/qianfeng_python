# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:31:48 2018

@author: jixiaoyun
"""


import urllib.request
import os
import re

#打开url操作
def url_open(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36','Referer': 'http://wwww.mzitu.com'}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

#获取当前图片组的最大页码数
def get_maxpage(url):
    html = url_open(url).decode('utf-8')
    pages = re.findall(r'<span>\d{1,2}',html)
    return pages[-1][6:len(pages[-1])]

#传入当前页面url，返回当前页面所有图片组链接地址列表
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    imgs_url = re.findall(r'http://www.mzitu.com/\d{6}',html)
    return imgs_url

#传入图片组url，返回图片组中所有图片链接地址列表
def find_img(url,page):
    html = url_open(url + '/' + str(page)).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg" alt="',a,a+255)
        if b!= -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b =a + 9
        a = html.find('img src=',b)
    return img_addrs[0]


#根据图片地址列表，将图片保存到folder中
def save_img(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        print(filename)
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def download(folder = 'meizi',*pages):
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    url = 'http://www.mzitu.com'
    # page_num = int(get_page(url))        #获取当前页数

    for page in pages:
        page_url = url + '/page/' + str(page) + '/'
        #创建页文件夹
        pagefolder = "page-" + str(page)
        if not os.path.exists(pagefolder):
            os.mkdir(pagefolder)
        os.chdir(pagefolder)
        #获取图片组地址列表
        img_group_addrs = find_imgs(page_url)
        #对于每个图片组，获取图片地址并保存
        group = 0
        for addr in img_group_addrs:
            group += 1
            img_addrs = [find_img(addr,x) for x in range(int(get_maxpage(addr)))]
        #创建组文件夹
            groupfolder = str(page) + "-" + str(group)
            if not os.path.exists(groupfolder):
                os.mkdir(groupfolder)
            os.chdir(groupfolder)
            save_img(groupfolder,img_addrs)
            os.chdir(os.pardir)
        os.chdir(os.pardir)

if __name__ == '__main__':
    download('meizi',1)#第一个参数为文件夹名，第二个参数为要爬取的页码