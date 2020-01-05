num = 7
while True:
    guess = int(input('请输入你猜的数（0～9）：'))
    if guess == num:
        print("恭喜！你猜中了！")
        break
    elif guess > num:
        print("太大")
    else:
        print("太小")
