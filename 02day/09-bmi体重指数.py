class tz():
    def zs(self):
        weight = float(input("请输入你的体重"))
        height = float(input("请输入你的身高"))
        bmi = weight/height**2
        print(bmi)
        if bmi < 18:
            print("过轻")
        if bmi >= 18 and num < 25:
            print("正常")
        if bmi >= 25 and num < 28:
            print("过重")
        if bmi >= 28 and num <= 32:
            print("肥胖")
        if bmi >= 32:
            print("严重肥胖")
ls = tz()
ls.zs()
