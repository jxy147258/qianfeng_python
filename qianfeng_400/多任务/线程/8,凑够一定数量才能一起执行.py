'''
bar = threading.Barrier(2)
凑够2个数量之后才能运行bar.wait()之后的语句，凑不够就一直等
'''


import  threading,time

bar = threading.Barrier(2)


def run():
    print("%s---开始"%(threading.current_thread().name))
    time.sleep(1)
    bar.wait()
    # 根据开头的说明，一共5个线程，凑够两个才能运行以下语句，所以一定会有一个线程因为凑不够而阻塞
    print("%s---结束"%(threading.current_thread().name))


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()