import time

def timeme(X):
    
    print('Total time ', elapsed())

def elapsed():
    a = time.time()
    time.sleep(2)
    b = time.time()
    c = b-a
    return c


timeme(elapsed)

