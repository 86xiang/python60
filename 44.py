import math


def shushu(n):
    i, w = 2, 0
    if n <= 1:
        w = 1
    while i <= int(math.sqrt(n)) and w == 0:
        if n % i == 0:
            w = 1
        break
    else:
        i = i + 1
    return w


n = int(input('n='))
if shushu(n) == 0:
    print(n, "是素数！")
else:
    print(n, "不是素数！")
