import random

x = [random.randint(0, 100) for i in range(1000)]
d = set(x)
for v in d:
    print(v, ':', x.count(v))
