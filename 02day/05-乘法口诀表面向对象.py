'''
class mouse:
    def lei(self):
        for i in range(10):
            for j in range i:
                if i*j= k:
                    print("%d * %d = %d"%(i,j,k),end=\n)
ls = mouse()
ls.lei()
'''
class mouse():
    def lei(self):
        i = 1
        while i < 10:
            j = 1
            while j <= i:
                d = i * j
                print("%d * %d = %d"%(i,j,d), end = "\t ")
                j+=1
            print(" ")
            i+=1
ls = mouse()
ls.lei()
