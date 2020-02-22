import threading


local_school = threading.local()


def process_student():
    std = local_school.name
    print(' %s is in %s ' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.name = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('alice',), name='thread_a')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='thread_b')
t2.start()
t1.start()
t1.join()
t2.join()
