#
import re
import os
import urllib.request


def getHTML(url):
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0"
        }
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    htmlInfo = resp.read().decode("utf-8")
    return htmlInfo

# 分离链接url的re语句
rootSite = r"http://xxee11.com/Pic1"
getHTML(rootSite)
siteUrl_re =re.compile(r"href=\"(.*?)\"")
jpgUrlList = siteUrl_re.findall()
print(jpgUrlList)

j=1
for singleJpgUrl in jpgUrlList:
    toPath = r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫"
    jpgInfo = getHTML(singleJpgUrl)
    print(jpgInfo)
    jpg_re = re.compile(r"src=\"(.*?)\"")
    jpg_url = jpg_re.findall(jpgInfo)
    imgInfo = getHTML(jpg_url)
    absPath = os.path.join(toPath,str(j)+".jpg")
    with open(absPath,"wb") as f:
        f.write(imgInfo)