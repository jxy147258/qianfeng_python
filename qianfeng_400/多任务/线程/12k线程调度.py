import threading

cond = threading.Condition()

def run():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            cond.wait()
            cond.notify()


def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name,i)
            cond.notify()
            cond.wait()

threading.Thread(target=run).start()
threading.Thread(target=run2).start()
