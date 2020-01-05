def money():
    while True:
        try:
            x = int(input("请输入本周常规工作时间(小时）："))
            if x < 0:
                print("一周常规工作时间不能小于0小时！")
            elif x > 40:
                print("一周常规工作时间不能超过40小时！")
            else:
                break
        except ValueError:
            print("输入错误！请输入整数！")

    while True:
        try:
            y = int(input("请输入本周加班时间(小时）："))
            if y < 0:
                print("一周的加班时间不能小于0小时！")
            else:
                break
        except ValueError:
            print("输入错误！请输入整数！")

    while True:
        try:
            z = float(input("请输入您的时薪："))
            if z < 0:
                print("您的时薪工资不能小于0！")
            else:
                break
        except ValueError:
            print("输入错误！请输入整数！")
    print("-" * 30)
    print("您的常规上班时间是：%d小时" % x)
    print("您的加班时间是：%d小时" % y)
    print("您的时薪是：%.2f元/小时" % z)
    print("您的周工资是：%.2f元" % ((x * z) + (y * 1.5 * z)))


if __name__ == "__main__":
    money()
