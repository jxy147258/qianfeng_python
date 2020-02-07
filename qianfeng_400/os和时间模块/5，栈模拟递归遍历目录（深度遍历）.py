#队列先进先出，适用于广度优先，栈先进后出，适用于深度优先
import os


def getAllDirDE(path):
    stack = []
    #把初始目录压栈，然后处理栈，如果是目录就压栈，如果是普通文件就打印名称
    stack.append(path)
    print("初始化栈：",stack)


    #处理栈，边界条件是栈为空，则结束循环
    while len(stack) != 0: #栈不空说明，栈中有一个目录，
        dirpath = stack.pop()
        print("栈顶元素:"+dirpath)
        fileList = os.listdir(dirpath) # 是目录就列出目录中所有文件
        print("当前目录中列表:",fileList)
        for fileName in fileList:
            fileAbspath = os.path.join(dirpath,fileName)
            if os.path.isdir(fileAbspath):
                print("目录："+fileName)
                stack.append(fileAbspath)
            else:
                print("普通文件："+fileName)
        print("处理后：",stack)


getAllDirDE(r"F:\python_G\python_shell\venv")