f = open("score2.txt")
a = f.readlines()
del a[0]
L2 = []
L3 = []
for line in a:
    line = line.strip()
    L1 = line.split()
    L2.append(L1[0])
    L3.append(L1[1])
f.close()
maxScore = L3[0]
maxIndex = 0
minScore = L3[0]
minIndex = 0
for i in range(1, len(L3)):
    if L3[i] > maxScore:
        maxScore = L3[i]
        maxIndex = i
    if L3[i] < minScore:
        minScore = L3[i]
        minIndex = i
print("最高分为：" + str(maxScore) + "分，该学生学号为：" + str(L2[maxIndex]))
print("最低分为：" + str(minScore) + "分，该学生学号为：" + str(L2[minIndex]))
