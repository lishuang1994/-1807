class Dog():
    def __init__(self):
        self.name = name
        print("长瑞线")
    def __str__(self):
        msg = "我的名字是%"%self.name
        return msg
    def __del__(self):
        print("我要删除了")
dog = Dog("长睿线")
print(self.name)
dog1 = dog
del dog
print("我爱你")

