import time,threading


def loop():
    print("current thread is %s" % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('%d current thread is %s start' % (n,threading.current_thread().name))
        time.sleep(1)
    print('current thread is %s end'%threading.current_thread().name)


print("thread %s is start" % (threading.current_thread().name))
tr = threading.Thread(target=loop())
tr.start()
tr.join()
print("thread %s is end" % (threading.current_thread().name))