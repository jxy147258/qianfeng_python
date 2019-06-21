from urllib import urlopen
from bs4 import BeautifulSoup
import re

for page in range(17):
    if page == 0:
        continue
    firstUrl = "http://new.bj.xdf.cn/zhentiku/daxue/kaoyan/kyzyk/list_381_" + str(page) + ".html"
    print "[Begin] scrap page", firstUrl
    html = urlopen(firstUrl)
    data = html.read()
    bsobj = BeautifulSoup(data)

    li = bsobj.findAll("a", {"title": re.compile(u"(.*?)新闻(.*?)")})

    for l in li:
        url = "http://new.bj.xdf.cn" + l.attrs["href"]
        filename = l.attrs["title"] + ".html"
        subdata = BeautifulSoup(urlopen(url).read())
        with open(filename, 'w') as f:
            f.write('<meta charset=\"UTF-8\">\n')
            f.write('%s' % subdata.select(".article-wrap"))
            f.close()
    print "[End]" 