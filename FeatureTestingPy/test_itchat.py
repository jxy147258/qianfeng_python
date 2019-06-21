import itchat
from pandas import DataFrame
import jieba
import re
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)


NickName = []
Sex = []
Province = []
City = []
Signature = []


for friend in friends:
    NickName.append(friend['NickName'])
    Sex.append(friend['Sex'])
    Province.append(friend['Province'])
    City.append(['City'])
    Signature.append(friend['Signature'])
dic = {'NickName': NickName, 'Sex': Sex, 'Province': Province, 'City': City, 'Signature': Signature}
# 然后将它存为DataFrame：
data = DataFrame(dic)
# 保存为一个excel文档保存到本地：
# data.to_csv('data.csv', index=True, encoding='utf_8_sig')


# 性别比例
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# sexcounts = data['Sex'].value_counts()
# sexcounts.plot(kind='pie', autopct='%1.0f%%', pctdistance=0.5, labeldistance=1.2).get_figure()
# plt.show()


# 地域分布
# procounts = data['Province'].value_counts()
# procounts.plot(kind='bar').get_figure()
# plt.show()

# 签名词云图
text = ''.join(Signature)
reg = re.compile('<span .*?>(.*?)</span>')
text = reg.sub('', text)

wordlist = jieba.cut(text, cut_all=True)
words = ' '.join(wordlist)
coloring = np.array(Image.open('w.jpg'))
# my_wordcloud = WordCloud(background_color='white', max_words=2000, mask=coloring, max_font_size=60, random_state=42,
#                          scale=2, font_path='/Library/Fonts/Microsoft/SimHei.ttf').generate(words)
my_wordcloud = WordCloud(
    background_color="white",
    width=1000,
    height=860,
    font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",#不加这一句显示口字形乱码
    margin=2).generate(words)
# image_colors = WordCloud.ImageColorGenerator(coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()