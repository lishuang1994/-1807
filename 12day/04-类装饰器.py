class Dog():
    def __init__(self,fun):
        self.fun = fun
    def __call__(self):
        print("验证")
        self.fun()

@Dog
def test():
    print("哈哈哈")
test()
