f = open("score1.txt")
a = f.readline()
line = (f.readline()).strip()
f2 = open("score2.txt", 'w')
f2.write("学号 平均成绩\n")
L2 = [0, 0, 0, 0, 0]
count = 0
sum = 0
while len(line) != 0:
    # print(line)
    L1 = line.split()
    f2.write(L1[0] + " ")
    f_score = int(int(L1[1]) * 0.4 + int(L1[2]) * 0.6)
    if 90 < f_score <= 100:
        L2[0] += 1
    elif f_score >= 80:
        L2[1] += 1
    elif f_score >= 70:
        L2[2] += 1
    elif f_score >= 60:
        L2[3] += 1
    else:
        L2[4] += 1
    count += 1
    sum += f_score
    f2.write(str(f_score) + "\n")
    line = (f.readline()).strip()
f.close()
f2.close()
avg_score = int(sum / count)
print("学生总人数为%d，按总评成绩计,90以上%d人、80～89间%d人、70～79间%d人、60～69间%d人、60分以下%d人。班级总平均分为%d分。" % (
    count, L2[0], L2[1], L2[2], L2[3], L2[4], avg_score))

'''
f = open("score1.txt")
a = f.readlines()
del a[0]
L3 = []
for line in a:
    line = line.strip()
    L1 = line.split()
    f_score = int(int(L1[1]) * 0.4 + int(L1[2]) * 0.6)
    L3.append([L1[0], f_score])
f.close()
c = [0, 0, 0, 0, 0]
count = 0
sum = 0
f2 = open("score2.txt", 'w')
f2.write("学号 平均成绩\n")
for L2 in L3:
    if 90 < L2[1] <= 100:
        c[0] += 1
    elif L2[1] >= 80:
        c[1] += 1
    elif L2[1] >= 70:
        c[2] += 1
    elif L2[1] >= 60:
        c[3] += 1
    else:
        c[4] += 1
    count += 1
    sum += L2[1]
    f2.write(L2[0] + " " + str(L2[1]) + "\n")
f2.close()
avg_score = int(sum / count)
print("学生总人数为%d，按总评成绩计,90以上%d人、80～89间%d人、70～79间%d人、60～69间%d人、60分以下%d人。班级总平均分为%d分。" % (
    count, c[0], c[1], c[2], c[3], c[4], avg_score))
'''
