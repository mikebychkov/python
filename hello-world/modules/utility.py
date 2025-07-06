
print(__name__)

def m_multiply(num1, num2):
    return num1 * num2

def m_divide(num1, num2):
    return num1 / num2

def m_sum(*nums):
    rsl = 0
    for n in nums:
        rsl += n
    return rsl
