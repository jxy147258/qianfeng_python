from multiprocessing import Process
from multiprocessing import Pool
import os,random,time


def run(name):
    print("子进程%d--开始--%s"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("子进程%d--结束--%s--耗时%s"%(name,os.getpid(),end-start))

if __name__ == '__main__':
    print("父进程开始--%s"%(os.getpid()))

    # 创建进程池
    pp = Pool(4) # 4是同时可以进行的进程数量，默认值等于CPU核心数
    for i in range(5):
        # 创建进程，放入进程池统一管理
        pp.apply_async(run,args=(i,))
    # 也可以手动执行apply_async()
    # 必须先调用close关闭进程池，再调用join。所以调用close之后就不能再添加新进程
    pp.close()
    # 进程池对象调用join，会等待进程池中所有子进程结束后再去执行父进程的语句
    pp.join()

    print("父进程结束")


