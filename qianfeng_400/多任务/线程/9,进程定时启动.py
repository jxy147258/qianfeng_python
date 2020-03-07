import threading

def run():
    print("sunck is a good man ")

# 每执行一次就是生成一个线程
t = threading.Timer(5,run)
t.start()

t.join()

print("父线程结束")