import random
class DiGua():
    def __init__(self):
        self.status = "生的"
        self.times = 0
        self.zl = [] #装作料
    def __str__(self):
        msg = "我烤的程度是%s"%self.status
        return msg+str(self.zl)
    def cook(self,time):
        self.times+=time
        if self.times >= 1 and self.times <= 3:
            self.status = "我是生的"
        elif self.times >= 4 and self.times <= 6:
            self.status = "三分熟"
        elif self.times >= 7 and self.times <= 12:
            self.status = "八分熟"
        elif self.times >= 13 and self.times <= 15:
            self.times = "可以吃啦"
        elif self.times > 15:
            self.times = "我已经糊了"
    def addzl(self,name):
        self.zl.append(name)
list = ["糖","盐","番茄酱","黑胡椒","辣椒酱","孜然"]
digua = DiGua()
for i in range(5):
    digua.cook(random.randint(1,4))
    zl = random.choice(list)
    list.remove(zl)
    digua.addzl(zl)
    print(digua)
        

