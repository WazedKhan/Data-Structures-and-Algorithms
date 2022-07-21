import math

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True

print(is_prime(4))

# so the time complexity is O(sqrt(n))