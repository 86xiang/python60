def output_avg(L):
    sum1, sum2 = 0, 0
    for line in L:
        L1 = line.strip().split()
        sum1 += int(L1[1])
        sum2 += int(L1[2])
    count = len(L)
    avg1 = round(sum1 / count, 1)
    avg2 = round(sum2 / count, 1)
    print("这个班的数学平均分为：%4.1f，语文平均为：%4.1f" % (avg1, avg2))


def output_notpass(L):
    print("两门课均不及格的学生学号及数学、语文成绩为：")
    for line in L:
        L1 = line.strip().split()
        if int(L1[1]) < 60 and int(L1[2]) < 60:
            print(line)


def output_good(L):
    print("两门课平均分在90分以上的学生学号及数学、语文成绩为：")
    for line in L:
        L1 = line.strip().split()
        f_score = round((int(L1[1]) + int(L1[2])) / 2)
        if f_score >= 90:
            print(line)


f = open("class_score.txt")
L = f.readlines()
del L[0]
output_avg(L)
output_notpass(L)
output_good(L)
