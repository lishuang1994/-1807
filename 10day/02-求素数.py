class sushu():
    def qiu(self):
        for i in range(2,101):
            flag = 10
            for j in range(2,i):
                if i%j == 0:
                    flag = 0
                    break
            if flag == 10:
                print(i)
ls = sushu()
ls.qiu()
