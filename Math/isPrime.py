# if n is less or equal to 1 return Falsh
# if n is greater then 1 next step
# check if n is divisible by any number between 2 to n-1
# if not divisible return True
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(isPrime(int(input('Enter A Number: '))))

"""
Worst case is O(n) because the loop will run for n-2 times.

"""