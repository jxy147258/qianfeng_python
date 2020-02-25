import urllib.request



def yhdCrawler(url,toPath):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    htmlInfo = resp.read()
    return htmlInfo




url = r"https://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E8%25A3%2585"
toPath =r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫/aa44.html"

info = yhdCrawler(url,toPath)
with open(toPath, "wb") as f:
    f.write(info)