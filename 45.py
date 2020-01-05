def insertList(L1, x):
    if x > L1[len(L1) - 1]:
        L1.append(x)
        return
    for i in range(0, len(L1)):
        if x < L1[i]:
            L1.insert(i, x)
            break
    return


L1 = [1, 4, 6, 9, 13, 16, 28, 40, 100]
x = int(input('请输入一个要插入的整数：'))
insertList(L1, x)
print(L1)
