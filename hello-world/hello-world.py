print("Hello world!")

for i in [1, 2, 3]:
    print(i)

# TYPES

type(1) # int
type(1.2) # float
type("Whoa") # str
type('A') # str
type([]) # list
type(()) # tuple
type(True) # bool
type({1:"one", 2:"two"}) # dict
type({1, 2 , "qwas"}) # set
type(None)

# 

round(3.987) # 4
round(3.987, 2) # 3.99

abs(-5)

# STRINGS

s = "Whoa what's this"
len(s)

s[1]
s[-1]
s[1:]
s[5:10]
s[5:10:2]
s[::-1]

s.upper()
s.strip()

# LISTS

l = ['a', 'b', 'c', 12]
l_copy = l[:] # MAKE COPY OF A LIST
l_copy[3] = 'd'
print(f"list: {l}")
print(f"list copy: {l_copy}")

# UNPACKING

first, *other, last = l
print(first)
print(other)
print(last)
