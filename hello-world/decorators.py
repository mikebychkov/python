
## CUSTOM DECORATOR

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("=" * 10)
        func(*args, **kwargs)
        print("=" * 10)
    return wrap_func

@my_decorator
def hello_func(msg = "HELLO"):
    print(msg)

hello_func()

hello_func("YO, DUDE, WTF")


## 

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        print("START:", t1)
        rsl = fn(*args, **kwargs)
        t2 = time()
        print("END:", t2)
        print("TIME TOOK:", t2 - t1, "s")
        return rsl
    return wrapper

@performance
def long_func():
    s = 0
    for i in range(10000000):
        s += i ** 9
    return s

long_func()

## 

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wr(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print("USER IS NOT VALID!")
    return wr

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
