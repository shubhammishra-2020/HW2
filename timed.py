import time

def timeme(X):

    def elapsed():
        start = time.time()
        X()
        end = time.time()
        print(f"Total Time {end-start}")
    return elapsed() 