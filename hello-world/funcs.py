def hello(name, age):
    print(f"Hello, {name} of {age} years old!")

hello("Jake", 69)

hello(age = 23, name = "Sully")

def hello2(name = "John Doe", age = "dumb"):
    print(f"Hello, {name} of {age} years old!")

hello2()
hello2("Ivan", 33)
hello2("Didi")
hello2(age = 27)

###

def func1(num1, num2):
    def func2(num1, num2):
        return num1 + num2
    return func2

rsl = func1(1, 2)
print(rsl)
print(rsl(5, 5))

#

def func3(num1, num2):
    def func4():
        return num1 + num2
    return func4

rsl2 = func3(1, 2)
print(rsl2)
print(rsl2())
print(rsl2())
print(rsl2())

###

def some_func():
    """
    Read the fuckin manual
    """
    pass

some_func() # editor will show docstring

###

def many_arg(a, b, *other, x):
    print(a, b, other, x)

many_arg(1,2,3,4,x=99)

# 

def many_arg2(a, b, *other, **other2):
    print(a, b, other, other2)

many_arg2(1,2,3,4,99,f=32)

# 

def many_arg3(a, b, **other2):
    print(a, b, other2)

many_arg3(1,2,f=32)

# 

pi = 3.14

if (n := 222 * pi) > 1000:
    print("IF", n)
else:
    print("ELSE", n)

# 

q = 10

def qqq():
    q = 20

print(q)

qqq()

print(q)

