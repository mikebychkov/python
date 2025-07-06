
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

