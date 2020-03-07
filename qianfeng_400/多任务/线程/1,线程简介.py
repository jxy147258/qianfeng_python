'''
一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们吧进程内的这些“子任务”叫做线程
线程是共享内存空间的并发执行的多任务，每一个线程都共享一个进程的资源。

模块：
 _thread模块 低级模块
 threading 高级模块




'''

import threading
import time
a = 10
def run():
    print("子线程（%s）开始"%(threading.current_thread().name))
    print("打印")
    time.sleep(3)
    # 注意：a属于主线程内的数据，如果主线程执行结束，就会释放内存，如果此时子线程再去取a的值，就会报错，这个例子看不出来，遇到再说
    print(a)
    print("子线程（%s）结束"%(threading.current_thread().name))


if __name__ == '__main__':
    # 任何进程默认都会启动一个线程，称为主线程，主线程可以启动新的子线程
    print("主线程（%s）启动"%(threading.current_thread().name))

    # 创建子线程
    t = threading.Thread(target=run,name="runThread")
    t.start()

    t.join()


    print("主线程（%s）结束"%(threading.current_thread().name))