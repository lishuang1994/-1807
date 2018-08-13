class Dog():
    def __init__(self):
        self.name = ""
        self.__age = 0
    def setAge(self,age):
        if age > 15 or age < 1:
            print("不符合标准")
        else:
            self.__age = age
    def getAge(self):
        return self.__age
hsq = Dog()
hsq.setAge(10)
print(hsq.getAge())
