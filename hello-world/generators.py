
# range()

def fn_gen(n):
    for i in range(n):
        yield i

my_gen = fn_gen(10)
print(my_gen.__next__())
print(my_gen.__next__())
print(next(my_gen))
print(next(my_gen))
for n in my_gen:
    print("in loop", n)

### 

def my_iter(iterable):
    it = iter(iterable)
    while True:
        try:
            n = next(it)
            print(n)
            yield n 
        except StopIteration:
            break

li = my_iter([1,2,3,4])
for n in li:
    pass

st = my_iter("QWAS")
for n in st:
    pass

###

class MyGen:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            n = self.current
            self.current += 1
            return n
        raise StopIteration

gen = MyGen(1, 10)
for i in gen:
    print(i)


### fib1

class MyFib:

    def __init__(self):
        self.prev2 = 0
        self.prev1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        n = self.prev1 + self.prev2
        self.prev2 = self.prev1
        self.prev1 = n
        return n

fib = MyFib()
for i in range(20):
    print(i + 2, next(fib))

### fib2

def fib_calc(n):
    prev2 = 0
    prev1 = 1
    print(prev2)
    print(prev1)
    for i in range(n - 1):
        _ = prev1 + prev2
        prev2 = prev1
        prev1 = _
        print(_)

fib_calc(20)

### fib3

def fib_gen(n):
    prev2 = 0
    prev1 = 1
    print(prev2)
    print(prev1)
    for i in range(n - 1):
        _ = prev1 + prev2
        prev2 = prev1
        prev1 = _
        yield _

fib = fib_gen(20)
for i in fib:
    print(i)

### fib4

def fib_gen2(n):
    prev2 = 0
    prev1 = 1
    for i in range(n + 1):
        yield prev2
        _ = prev1 + prev2
        prev2 = prev1
        prev1 = _

fib = fib_gen2(20)
for i in fib:
    print(i)
