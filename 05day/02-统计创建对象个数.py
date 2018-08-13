class Phone():
    count = 0 #类方法
    def __init__(self,color):
        self.color = color
        Phone.count+=1
    def call(self):
        print("打电话")
xiaoming = Phone("白色")
xiaoming1 = Phone("黑色")
xiaoming2 = Phone("灰色")
print(Phone.count)
