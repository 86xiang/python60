flname = "temp.txt"
f = open(flname)
ht = (f.readline()).strip()
L1 = list(ht.split(','))
lt = (f.readline()).strip()
L2 = list(lt.split(','))
f.close()
L3 = []
for i in range(len(L1)):
    L1[i] = int(L1[i])
    L2[i] = int(L2[i])
    L3.append(int((L1[i] + L2[i]) / 2))
sum = 0
k = 0
for i in range(len(L3)):
    sum = sum + L3[i]
    if L3[i] >= 10:
        k += 1
    else:
        k = 0
avg = int(sum / len(L3))
print("周平均气温为：", avg)
if k >= 5:
    print("上海这周已入春。")
else:
    print("上海这周未入春。")
