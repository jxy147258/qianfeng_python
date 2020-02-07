'''
安装第三方包方法：
1，pip install pilow
2，如果报错升级pip，pip install --upgrade pip
3，安装的包的名称和import时的可能不同
'''
from PIL import Image

img = Image.open("18.PNG")
print(img.size,img.format,img.mode)
img.thumbnail((150, 100))
img.save("temp.jpg","PNG")