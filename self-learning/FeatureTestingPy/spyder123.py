# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import re
import os
import socket
#import time
import threading


def url_open(url):
    socket.setdefaulttimeout(20)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
    res = requests.get(url, headers=headers)

    return res


def save(url):  # 传入每个子网页链接
    res = url_open(url)
    res.encoding = 'gbk'
    soup = bs(res.text, 'lxml')
    title = soup.find('title').text.split('-')[0]  # 标题
    #os.mkdir(title)
    # os.chdir(title)
    temp = soup.find_all('tr', class_='tr3')
    img = re.findall(r'data-src="(.*?jpg)" type', str(temp))
    
    
    imglist = []

    for each in img:
        imglist.append(each)
    for each in imglist:
        filename = each.split('/')[-1]
        img = url_open(each)
        print('saving...+%s'%filename)

        with open(title+filename, 'wb')as f:
            f.write(img.content)
    #os.chdir('..')




if __name__ == '__main__':
    os.makedirs('1024', exist_ok=True)
    os.chdir('1024')
    url = 'https://cl.e7s.win/thread0806.php?fid=16&search=&page=1'  #默认爬取第一个页面，毕竟要注意身体，需要多个页面的话，自己加个for循环也不是什么难事~
    urlhead = 'https://cl.e7s.win/'   #页面解析出来的连接前面需要加上这个头才能打开，根据多年经验这个头是会变的，如果哪天不能用了自己看下是不是这个头变了
    res = url_open(url)
    res.encoding = 'gbk'

    '''找到页面中的所有子网页'''
    soup = bs(res.text, 'lxml')
    temp = soup.find_all('td', class_="tal")
    link = []
    for each in temp:
        link.append(urlhead + each.h3.a.get('href'))
    # del link[0:10]

    downloads = []
    for each in link:
        print(each)

        down = threading.Thread(target=save, args=[each])
        downloads.append(down)

        down.start()
    for each in downloads:
        each.join()
    print('Done')

