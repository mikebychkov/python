age = input("What is your age: ")
try:
    age = int(age)
except:
    print("Don't mess with me you punk!")
    exit()

if age == 25:
    print("Ou, cool, good for you!")
elif age > 30:
    print("You old")
elif age < 20:
    print("You young")
