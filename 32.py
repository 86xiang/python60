score = int(input('请输入成绩（0～100）：'))
if score > 100:
    grade = "输入错误！"
elif score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score >= 0:
    grade = 'E'
else:
    grade = "输入错误！"
print(grade)
