import urllib.request
import re
import os

def yhdCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    htmlInfo = resp.read().decode("utf-8")
    return htmlInfo


yhdUrl = r"https://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E8%25A3%2585/"
toPath = r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫/aa44.html"

htmlInfo = yhdCrawler(yhdUrl)
yhd_re = re.compile(r"<img src=\"//(.*?)\"/>")
imgurl = yhd_re.findall(htmlInfo)
# print(imgurl)
# print(len(imgurl))



j=1
for i in imgurl[0:12]:
    imgPath = r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    }

    url = "http://" + i
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    htmlInfo = resp.read()
    # imgPath的值每次都要变，不要积累前面的结果，所以写在循环外面。j的值需要积累前面的结果，所以写在循环外
    imgPath = os.path.join(imgPath,str(j)+".jpg")
    j += 1
    with open(imgPath,"wb") as f:
        f.write(htmlInfo)