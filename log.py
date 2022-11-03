import time

def timestamp(X):
    print(decoTime())
    print('hi')

def decoTime():
    c = time.ctime()
    return c

timestamp(decoTime)
