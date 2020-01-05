def ball():
    while True:
        try:
            x = int(input("请输入弹跳次数："))
            if x < 0:
                print("弹跳次数不能小于0！")
            start_lang = float(input("请输入初始高度："))
            if start_lang <= 0:
                print("初始高度必须大于0！")
            while x > 0:
                end_lang = start_lang * 0.6
                start_lang = start_lang + end_lang
                x = x - 1
            print("弹跳总长度：%.2f" % (start_lang))
            break
            break
        except ValueError:
            print("输入错误，请从新输入!")


ball()
