class shitou():
    def jiandao(self):
        import random
        while True:
            cp = random.randint(1,3)
            py = int(input("1:石头2:剪刀3:布"))
            if (cp == 1 and py == 3) or (cp == 2 and py == 1) or (cp == 3 and py == 2):
                print("玩家赢了")
            elif cp == py:
                print("平局")
            else:
                print("电脑赢了")
ls = shitou()
ls.jiandao()
