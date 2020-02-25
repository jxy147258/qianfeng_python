import urllib.request
import re



def zhongJoke(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}
    req = urllib.request.Request(url,headers=headers)

    resp = urllib.request.urlopen(req)
    respinfo = resp.read()
    HTMLinfo = respinfo.decode("GBK")
    # TODO 测试HTMLinfo是什么类型
    # print(type(HTMLinfo)) # HTMLinfo是bytes类型，按理说可以用decode解码
    return HTMLinfo,respinfo


url = r"http://xiaohua.zol.com.cn/detail32/31672.html"
oriInfo,jsonInfo = zhongJoke(url)
print(type(oriInfo),type(jsonInfo))

# html_re = re.compile(r'<div class="article-text">\n\t'<p>(.*?)<p></p>',re.S)
html_re = re.compile(r'<div class="article-text">\s{26}<p>(.*?)<p></p>(.*?)</p>',re.S)
print(html_re.findall(oriInfo))


# 先一行一行读出来内容
# 如果检测到<div class="article-text"> 就停止
# 并读出内容
# 另一个网站https://saohu133.com/photo/4132




























