def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

line = line_conf(2,3)
print(line(5))
