d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
v = input('Please input a key:')
v = eval(v)
print(d.get(v, '您输入的的键不存在'))
