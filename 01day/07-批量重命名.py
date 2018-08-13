import os
name = input("请输入你要重命名文件夹的名字")
files = os.listdir(name)
os.chdir(name)

for i in files:
    position = i.rfind(".")
    newname = i[:position] + "-王者荣耀" + i[position:]
    os.rename(i,newname)
