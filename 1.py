x = input('Please input an integer of more than 3 digits:')
try:
    x = int(x)
    x = x // 100
    if x == 0:
        print('You must input an integer of more than 3 digits.')
    else:
        print(x)
except BaseException:
    print('You must input an integer.')
