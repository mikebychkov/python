# map, filter, zip, reduce

l = [1,2,3,4,5,6,7,8,9]

###

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


########

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

########

from functools import reduce

s = reduce(lambda x,y: x + y, l, 0)
print(s)

########

list1 = [(4,3),(0,2),(10,-1),(9,9)]
list1.sort()
print(list1)

list1.sort(key=lambda x: x[1])
print(list1)

########


