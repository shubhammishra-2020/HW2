import time

def timeme(func):

    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print('Total time %s' % (end - start))
        return result
    return wrapper
