import pdb

def add(num1, num2):
    print("Debug message")
    pdb.set_trace() # interactive debugging - "help" - command while debug
    return num1 + num2

add(2, "qwas")

## pdb commands
# step 
# continue
# list - list the code that is debugged
# a - list all vars with values
# w - current context
