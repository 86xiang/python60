import math


def IsPrime(v):
    n = int(math.sqrt(v) + 1)
    for i in range(2, n):
        if v % i == 0:
            return 'No'
    else:
        return 'Yes'


print(IsPrime(37))
print(IsPrime(60))
print(IsPrime(113))
