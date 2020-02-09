def log(fn):
    def innner_func():
        print("begin call:",fn.__name__)
        fn()
        print("end call:",fn.__name__)
        return fn
    return innner_func


@log
def f():
    print("i am f()")



f()
