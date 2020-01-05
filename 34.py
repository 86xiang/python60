import math

n = int(input("请输入一个数:"))
x = int(math.sqrt(n))
i, w = 2, 0
for i in range(2, x + 1):
    if n % i == 0:
        w = 1
if w == 1:
    print(n, "不是素数。")
else:
    print(n, "是素数。")

'''
import math

n = int(input('请输入一个数：'))
i, w = 2, 0
while i <= int(math.sqrt(n)) and w == 0:
    if n % i == 0:
        w = 1
        break
    else:
        i = i + 1
if w == 0:
    print(n, "是素数！")
else:
    print(n, "不是素数！")
'''