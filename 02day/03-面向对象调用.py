class proson:
    def eat(self):
        print("吃饭")
    def sleep(self):
        print("睡觉")
    def da(self):
        print("打豆豆")
    def inturduce(self):
        print("我的身高是%d 我的体重是%d"%(self.height,self.weight))
ls = proson()
ls.eat()
ls.sleep()
ls.da()
ls.height = 180
ls.weight = 130
ls.inturduce()

ln = proson()
ln.eat()
ln.sleep()
ln.da()
ln.height = 190
ln.weight = 140
ln.inturduce()

