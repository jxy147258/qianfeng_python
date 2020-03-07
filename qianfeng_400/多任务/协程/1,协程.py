def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30
    
    
m = run()
print(next(m))
print(next(m))
print(next(m))