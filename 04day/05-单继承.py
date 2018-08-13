class Car(object):
    def __init__(self,name,money):
        self.name = name
        self.money = money
    def run(self):
        print("车在跑")
    def wark(self):
        print("滴滴滴")
class zixingche(Car):
    pass
class lieche(Car):
    pass
class huoche(Car):
    pass

fll = Car("本田",10000)
print(fll.name)
print(fll.money)
a = zixingche("山地",500)
a.run()
a.wark()
f = lieche("列车",299999)
f.run()
f.wark()
l = huoche("火车",444444)
l.run()
l.wark()
