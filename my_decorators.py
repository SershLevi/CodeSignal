def pd(func):
    def wrapper(*args, **kwargs):
        print("Execute [", func.__name__, "] with parameters", *args, **kwargs)
        a = func(*args, **kwargs)
        print(a)
    return wrapper
