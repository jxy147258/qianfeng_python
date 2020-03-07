# 没有锁机制情况下多进程共享数据会出错

import threading


num = 100
def run(n):
    global num
    for i in range(10000000):
        num += n
        num -= n
if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(6,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num = ",num)