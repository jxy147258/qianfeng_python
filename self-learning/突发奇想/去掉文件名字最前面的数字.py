import os


path = "/home/jixy2/BigFiles/光收藏不看系列/Data structure and algorithm (Python)"

fileList = os.listdir(path)

for i in fileList:
    # print(i)
    hou = i.split(".", maxsplit=1)
    print(hou[1])
    os.rename(os.path.join(path, i), os.path.join(path, hou[1]))





