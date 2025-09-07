import time


def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            print(args)
            return cache_value[args]
        
        result = func(*args)
        cache_value[args] = result
        print(cache_value[args])
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 4))
print(long_running_function(2, 4))
print(long_running_function(2, 5))