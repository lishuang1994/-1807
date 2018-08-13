class Car():
    def __init__(self,color,types):
        self.color = color
        self.types = types
    def __str__(self):
        msg = "我的颜色是%s 我的型号是%s"%(self.color,self.types)
        return msg
    def run(self):
        print("车在跑")
    def mouse(self):
        print("车在听音乐")
bmw = Car("黄色","x6")
bmw.run()
bmw.mouse()
print(bmw)
