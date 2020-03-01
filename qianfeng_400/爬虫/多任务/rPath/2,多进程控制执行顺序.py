from multiprocessing import Process
from time import sleep
import os

def run(str):
    print("子进程启动。。")
    sleep(3)
    print("子进程结束。。")



if __name__ == "__main__":
    print("主进程启动。。。")

    p = Process(target=run,args=("fuck",))
    p.start()

    # 父进程的结束不会影响子进程
    p.join() # join函数是让父进程等待所有子进程都结束后再继续执行父进程中的语句
    print("主进程结束。。")

