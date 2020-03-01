from multiprocessing import Process
import os,time



def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")

    context = fr.read()
    fw.write(context)

    fr.close()
    fw.close()


rPath = r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫/多任务/rPath"
wPath = r"/home/jixy2/pycharm_projects/qianfeng_python-master/qianfeng_400/爬虫/多任务/toPath"

# 读取rPath下所有文件
fileList = os.listdir(rPath)

start = time.time()
for fileName in fileList:
    copyFile(os.path.join(rPath,fileName),os.path.join(wPath,fileName))
end = time.time()
print("耗时：%s"%(end-start))