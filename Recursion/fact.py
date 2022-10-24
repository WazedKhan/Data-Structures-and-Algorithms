def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1: return 1

    else:
        val = (x * factorial(x-1))
        print(val)
        return val

print(factorial(5), 'Returned')