import re

info =  r'''<div class="article-text"> 
                        <p>夏天挨蚊子咬了，肿起来了，喜欢用手指掐出十字花，觉得那样痛快，痒得轻。<p></p>'''


html_re = re.compile(r'<div class="article-text">\s{26}<p>',re.S)
print(html_re.findall(info))