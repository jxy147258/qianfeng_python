'''
作业要求，
1, 读取一个文件，根据邮箱后缀新进一个目录，并在目录中生成一个txt，并把同类邮箱后缀写入
2, 读取一个文件，输入一个姓名，根据此姓名输出kaifang信息
3, 队列先进先出，适用于广度优先，栈先进后出，适用于深度优先
'''

import os
import collections


def handletxt(path):
    respath = r"F:\python_G\python_shell\qianfeng_400\os和时间模块\res"
    with open(path,"r",encoding="utf-8") as f:
        while True:
            eachline = f.readline()
            if len(eachline) < 5:
                break
            mailstr = eachline.split("-")[0]  #将来写入到txt中的内容
            fileType = eachline.split("-")[0].split("@")[1].split(".")[0]#分离出163后缀，下一步就合成\163路径
            dirstr = os.path.join(respath,fileType) #合成的目录的绝对路径
            if not os.path.exists(dirstr):
                os.mkdir(dirstr)
            filepath = os.path.join(dirstr,fileType+".txt")#合成的\163\XX.txt
            with open(filepath,"w") as fw:
                fw.write(mailstr+"\n")

            
def getAlldirQU(path):
    queue = collections.deque()
    queue.append(path)


    while  len(queue) != 0:
        dirpath = queue.popleft()
        filesList = os.listdir(dirpath)
        for fileName in filesList:
            fileAbspath = os.path.join(dirpath,fileName)
            if os.path.isdir(fileAbspath):
                # print("目录：",fileName)
                queue.append(fileAbspath)
            else:
                # print("普通：",fileName)
                handletxt(fileAbspath)
getAlldirQU(r"F:\python_G\python_shell\qianfeng_400\os和时间模块\newdir")

# readtxt(r"F:\python_G\python_shell\qianfeng_400\os和时间模块\kaifang.txt")
