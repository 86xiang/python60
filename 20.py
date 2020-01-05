import pickle

f = open(r'd:\1.txt', 'r')
s = f.readlines()
f.close()

r = [i.swapcase() for i in s]

f = open(r'd:\2.txt', 'w')
f.writelines(r)
f.close()

d = {'张三': 98, '李四': 90, '王五': 100}
print(d)
f = open('score.dat', 'wb')
pickle.dump(1, f)
pickle.dump(d, f)
f.close()

f = open('score.dat', 'rb')
pickle.load(f)
d = pickle.load(f)
f.close()
print(d)
