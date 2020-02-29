#
import re
import os
import urllib.request
import ssl

def getHTML(url):
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0"
        }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    resp = urllib.request.urlopen(req,context=context)
    htmlInfo = resp.read().decode("utf-8")
    return htmlInfo

# 分离链接url的re语句
rootSite = r"https://xxee11.com/htm/Picture1/3.htm"
rootInfo = getHTML(rootSite)
siteUrl_re =re.compile(r"href=\"/htm/Pic1(.*?)\"")
jpgUrlList = siteUrl_re.findall(rootInfo)
for i in jpgUrlList:
    allUrl = "https://xxee11.com/htm/Pic1"+i
    print(allUrl)
    for j in allUrl:
        threeUrl = getHTML(allUrl)
        three_re = re.compile(r"src=\"https:\/\/ppp\.kyj29\.com(.*?)\">")
        jpgUrl = three_re.findall(threeUrl)
        for k in jpgUrl:
            realjpgUrl = "https://ppp.kyj29.com/"+k
            print(realjpgUrl)


'''for i in jpgUrlList:
    allUrl = "https://xxee11.comhttps://xxee11.com"+i
    threeUrl = getHTML(allUrl)
    three_re = re.compile(r"src=\"https:\/\/ppp\.kyj29\.com(.*?)\">")
    jpgUrl = three_re.findall(threeUrl)


    count = 1
    for j in jpgUrl:
        realUrl = "https://ppp.kyj29.com"+j
        jpgInfo = getHTML(realUrl)
        toPath = r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫"
        absPath = os.path.join(toPath,count)
        with open(absPath) as f:
            f.write(jpgInfo)
            count += 1'''
