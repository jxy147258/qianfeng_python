import json
import ssl
import urllib.request
import urllib.parse


def Crawler(url):
    # 用url和headers构造req
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0"}
    req = urllib.request.Request(url, headers=headers)
    # 用req和context构造response
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    #
    jsonStr = response.read().decode("utf-8")
    # jsonData = json.loads(jsonStr)
    return jsonStr



'''url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
info = Crawler(url)
print(info)'''
for i in range(1,11):
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+str(i*20)+"&limit=20"
    info = Crawler(url)
    print(info)
