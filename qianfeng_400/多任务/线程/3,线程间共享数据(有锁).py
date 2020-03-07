# 有锁机制下多进程共享数据

import threading

# 创建锁对象
lock = threading.Lock()
num = 100
def run(n):
    global num
    # 先加锁再执行
    for i in range(10000000):
        with lock:
            num += n
            num -= n
        lock.acquire()
        # 等同于以下语句
        '''try:
            num += n
            num -= n
        finally:
            lock.release()'''
if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(6,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num = ",num)