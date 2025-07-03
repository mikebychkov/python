# map, filter, zip, reduce

l = [1,2,3,4,5,6,7,8,9]


### MAP, FILTER

def is_even(n):
    return n % 2 == 0

nl = filter(is_even, l)

print(list(nl))

###

nl = filter(lambda n: n % 2 == 0, l)

print(list(nl))

###

nl = map(lambda n: n * 2, filter(lambda n: n % 2 == 0, l))

print(list(nl))


######## ZIP

from itertools import zip_longest

m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k']
m2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'x', 'y', 'z']
m3 = ['a', 'b', 'c', 'd', 'e', 'f']

z = zip(m, l)
print(list(z))

z = zip(m2, l)
print(list(z))

z = zip(m3, l)
print(list(z))

z = zip(m3, l)
x1, x2 = zip(*z) 
print(x1, x2)


######## REDUCE

from functools import reduce

s = reduce(lambda x,y: x + y, l, 0)
print(s)


######## LAMBDA FOR SORTING

list1 = [(4,3),(0,2),(10,-1),(9,9)]
list1.sort()
print(list1)

list1.sort(key=lambda x: x[1])
print(list1)


######## LIST COMPREHENSIONS

hello_list = [char for char in "Hello"]
print(hello_list)

mult_list = [n * 2 for n in range(10)]
print(mult_list)

power_list = [n ** 2 for n in range(10) if n % 2 == 0]
print(power_list)


######## SET COMPREHENSIONS (ALL THE SAME BUT {} INSTEAD ())

hello_list = {char for char in "Hello"}
print(hello_list)

mult_list = {n * 2 for n in range(10)}
print(mult_list)

power_list = {n ** 2 for n in range(10) if n % 2 == 0}
print(power_list)


######## DICT COMPREHENSIONS

simple_dict = {'a': 1, 'b': 2}
power_dict = {k:v ** 2 for k, v in simple_dict.items()}
print(power_dict)

dict2 = {n:n**2 for n in l}
print(dict2)


# Find duplicates

l = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Result should be ['b', 'n']

dups = {c for c in l if l.count(c) > 1}
print(dups)

