# Calculate the time of any method 
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} run in: {end - start}sec")
        return result
    return wrapper


@timer
def example_fucntion(n):
    time.sleep(n)

example_fucntion(2)