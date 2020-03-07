import threading,time


def func():
    # 创建事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            # wait是阻塞线程，等待事件去触发
            event.wait()
            # 重置阻塞，如果没有clear，触发一次以后就全部
            # 触发函数是event.set() 
            event.clear()
            print("sunck is a good man--%d"%(i))
    t = threading.Thread(target=run).start()
    return event

e = func()

# 触发事件
for i in range(5):
    time.sleep(2)
    e.set()