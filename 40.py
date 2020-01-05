f = open("sample12.txt")
L1 = f.readlines()
f2 = open("sample12_copy.txt", 'w')
for line in L1:
    f2.write(line.upper())
f.close()
f2.close()
