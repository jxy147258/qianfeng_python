'''
multiprocessing库
linux支持C语言中的fork函数，windows不支持fork函数，此库用Process类支持进程对象


'''

from multiprocessing import Process
from time import sleep
import os

def run(str):
    while True:
        print("sunck is a %s man !---%s--%s"%(str,os.getpid(),os.getppid()))
        sleep(1.2)


if __name__ == "__main__":
    print("父(主)进程启动。。。%s--%s"%(os.getpid(),os.getppid()))

    # 创建子进程
    p = Process(target=run,args=("fuck",)) # target指定子进程函数
    # 启动子进程
    p.start()  # 代码执行到这个位置就走向子进程函数去执行，主进程继续往下进行。
    while True:
        print("sunck is a good man !")
        sleep(1)
