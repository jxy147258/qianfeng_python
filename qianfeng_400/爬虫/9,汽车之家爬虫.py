#!/home/jixy2/pycharm_projects/qianfeng_python-master/venv/bin/python3.6
import urllib.request
import json
import ssl

# headers = "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0"
def motoHome(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}
    req = urllib.request.Request(url,headers=headers)

    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)

    jsonStr = response.read().decode("utf-8",errors="ignore")
    # jsonData = json.loads(jsonStr)
    with open(r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫/aa22.html","w") as f:
        f.write(jsonStr)



url = r"https://www.autohome.com.cn/dutu/873249.html#p=10"
motoHome(url)


'''for i in range(1,10):
    url = r"https://www.autohome.com.cn/dutu/873249.html#p="+str(i)
    info = motoHome(url)
    print(info)
'''