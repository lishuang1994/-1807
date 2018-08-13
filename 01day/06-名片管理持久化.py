list = [{"name":"老王","age":"18"},{"name":"老李","age":"21"}]
f = open("data.data","w")
f.write(str(list))
f.close()

list = []
f1 = open("data.data","r")
content = f1.read()
if len(content) !=0:
    print(type(content))
    list = eval(content)
    for i in list:
        for k,v in i.items():
            print(k,v)
        print(list)
f1.close()

