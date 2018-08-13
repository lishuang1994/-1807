class big():
    def small(self):
        import random
        i = 0
        number = random.randint(1,100)
        while i < 10:
            py = int(input("请输入数字"))
            if py > number:
                print("输入大了")
            elif py < number:
                print("输入小了")
            else:
                print("猜对了")
                i = 10
            i+=1
ls = big()
ls.small()
