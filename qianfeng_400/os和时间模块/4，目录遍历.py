import os


def getalldir(path,sp=""):
    fileslist = os.listdir(path)
    sp += "    "
    for filename in fileslist:
        fileAbspath = os.path.join(path,filename)
        if os.path.isdir(fileAbspath):
            print(sp + "目录：",fileAbspath)
            getalldir(fileAbspath,sp)
        else:
            print(sp + "普通 文件：",filename)

getalldir(r"F:\python_G\python_shell\venv")