import time
def timestamp(X):
    def wrapTime():
        print(time.ctime())        
        X()
    return wrapTime

