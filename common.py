from time import time_ns

def timer(func):
    def inner(*args, **kwargs):
        start = time_ns()
        res = func(*args, **kwargs)
        end = time_ns()
        print(f'{func.__name__} ran in {(end - start)/10**9:.2f} seconds')
        return res
    return inner
