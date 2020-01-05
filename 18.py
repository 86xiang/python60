def Sum(v):
    s = 0
    for i in v:
        s += i
    return s


x = [1, 2, 3, 4, 5]
print(Sum(x))
x = (1, 2, 3, 4, 5)
print(Sum(x))
