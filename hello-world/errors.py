
try:
    print("Hello" + 1)
except:
    print("Something went wrong")


### 

while True:
    try:
        age = int(input("Enter your age: "))
        10 / age
    # except ValueError:
    #     print("Please enter the number")
    # except ZeroDivisionError:
    #     print("Please enter not zero number")
    except (ValueError, ZeroDivisionError) as e:
        print(e)
    else:
        print("Thank you")
        break
    finally:
        print("Try block is done")
    
### 

def my_sum(n1, n2):
    try:
        return n1 + n2
    except Exception as e:
        print("Something went wrong:", e)

print(my_sum('1', 2))


### 

def my_fn(inputStr):
    if type(inputStr) != type(""):
        raise Exception("This is not a string")
    return f"This is your string: {inputStr}"

print(my_fn(1))
print(my_fn('1'))

