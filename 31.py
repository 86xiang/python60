cunkuan = 10000  # 本金10000元
years = 0
while cunkuan < 20000:
    years += 1
    cunkuan = cunkuan * (1 + 0.0325)
print(str(years) + "年以后，存款会翻番")
