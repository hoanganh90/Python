from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f'Performance: {end - start} seconds')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000):
        i * 5
@performance
def long_time2():
    print('2')
    for i in range(100000):
        i * 5
long_time()
long_time2()