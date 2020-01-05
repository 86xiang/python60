letters, space, digit, other = 0, 0, 0, 0
s = input("请输入一行字符：")
for i in range(len(s)):
    if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
        letters += 1
    elif s[i] == ' ':
        space += 1
    elif s[i] >= '0' and s[i] <= '9':
        digit += 1
    else:
        other += 1
print("字母数：%d\n空格数：%d\n数字数：%d\n其他字符数：%d\n" % (letters, space, digit, other))
