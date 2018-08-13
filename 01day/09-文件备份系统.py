#1.获取用户要复制的文件名
old_file_name = input("请输入要复制的文件名")

#2.打开要复制的文件
old_file = open(old_file_name,"r")

#3.新建一个文件
new_file = open("新建.txt","w")

#4.从旧文件中读取数据，并且写入新的文件中
content = old_file.read()
new_file.write(content)

#5.关闭两个文件
old_file.close()
new_file.close()
