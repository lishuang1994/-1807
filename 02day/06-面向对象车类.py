class car():
    def __init__(self,color,types,name,num):
        self.color = color
        self.types = types
        self.name = name
        self.num = num
    def moves(self):
        print("我的速度超快的")
    def music(self):
        print("在你的心上，自由的飞翔")
'''
    def introduce(self):
        print("我的车颜色是%s 我的车型是%s 我的名字是%s 我的 我的车牌号是%d"%(self.color,self.types,self.name,self.num))
'''
luhu = car("黑色","x200","超帅气",8000)
luhu.moves()
luhu.music()
#luhu.name = "超帅气"
#luhu.num = 8000
#luhu.introduce()
