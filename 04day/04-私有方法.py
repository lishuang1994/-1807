class QQ():
    def __openvip(self):
        print("开通成功!")
    def chekqq(self,money):
        if money > 10:
            self.__openvip()
        else:
            print("充值的钱不够")
qq = QQ()
qq.chekqq(12)
qq1 = qq
qq1.chekqq(8)
        
