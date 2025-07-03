for i in "Be or not to be?":
    print(i)

for i in (1, "qwas", 2, 'B'):
    print(i)

for i in [1,2,5,6,9]:
    print(i)

num = 0
for i in range(100):
    num += 1
print(num)

for i in range(0, 10, 2):
    print(i)
    
for i in enumerate("qwas sawq"):
    print(i)

for i in enumerate("qwas sawq"):
    print(i)
else:
    print("Done with qwas")
    
x = 10
while x > 0:
    print(x)
    x -= 1
else:
    print("Only if loop is went to the end, without breaking")

# Find duplicates

d = {}
l = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
rsl = []
for i,n in d.items():
    if n > 1:
        rsl.append(i)
print("Duplicates is: ", rsl)

# Find duplicates 2

l = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
rsl = set()
for i in l:
    if l.count(i) > 1:
        rsl.add(i)
print("Duplicates is: ", list(rsl))
