flname = "temp.txt"
f = open(flname)
ht = (f.readline()).strip()
L1 = list(ht.split(','))
lt = (f.readline()).strip()
L2 = list(lt.split(','))
f.close()
for i in range(len(L1)):
    L1[i] = int(L1[i])
    L2[i] = int(L2[i])
maxVal = L1[0]
maxDay = 0
minVal = L2[0]
minDay = 0
for i in range(1, len(L1)):
    if L1[i] > maxVal:
        maxVal = L1[i]
        maxDay = i
    if L2[i] < minVal:
        minVal = L2[i]
        minDay = i
print("这周第" + str(maxDay + 1) + "天最热，最高" + str(maxVal) + "摄氏度")
print("这周第" + str(minDay + 1) + "天最冷，最低" + str(minVal) + "摄氏度")
