import time

def timeme(func):
    def wrapper(t):
        start = time.time()
        result = func(t)
        end = time.time()
        print('Total time %s' % (end - start))
        return result
    return wrapper
