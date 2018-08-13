name = input("请输入你要备份的文件的名字")
f = open(name,"r")
content = f.read()

position = name.rfind(".")
newname = name[:position] + "李李" + name[position:]

f1 = open(newname,"w")
f1.write(content)

f.close()
f1.close()
