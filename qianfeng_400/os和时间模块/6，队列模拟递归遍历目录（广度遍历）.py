#队列先进先出，适用于广度优先，栈先进后出，适用于深度优先
import os
import collections


def getAlldirQU(path):
    queue = collections.deque()
    queue.append(path)


    while  len(queue) != 0:
        dirpath = queue.popleft()
        filesList = os.listdir(dirpath)
        for fileName in filesList:
            fileAbspath = os.path.join(dirpath,fileName)
            if os.path.isdir(fileAbspath):
                print("目录：",fileName)
                queue.append(fileAbspath)
            else:
                print("普通：",fileName)

getAlldirQU(r"F:\python_G\python_shell\venv")
