sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        print(x)
        sum = sum + x
print("累加和是:", sum)
