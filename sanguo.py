# 读取任务名称
f = open('name.txt')
data = f.read()
print(data.split('|'))

# 读取兵器
f2 = open('weapon.txt')
i = 1
for line in f2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1

f3 = open('sanguo.txt')
print(f3.read().replace('\n',''))

# 定义函数
def func(filename):
    print(open(filename).read())


