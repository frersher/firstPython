# @author:chenbang
# @time: 2021/12/25

# present = input("hello ajajaj?\n")
# print(present)

# a = input('一个加数:')
# b = input('另一个加数:')
# print(a+b)
# print(int(a)+int(b))

# a,b = 10,20
# print('交换前:',a,b)
#
# a,b = b,a
# print('交换后:',a,b)

# lsit1 = [11,22,33,44]
# lsit2 = [11,22,33,44]
# print(lsit1 ==  lsit2)
# print(lsit1 is lsit2)
# print(lsit1 is not lsit2)


# i = 4
# j = 8
#
# print(i&j)
# print(j<<2)


# num = int(input("请输入一个数字\n"))
#
# if num%2 == 0:
#     print(num,'是偶数')
#     # print(num, '1是偶数')
# else:
#     print(num,"是计数")

# num_1 = int(input('输入第一个数字'))
# num_2 = int(input('输入第二个数字'))
#
# print((str(num_1)+'大于等于'+str(num_2)) if num_1 >= num_2 else (num_1,'小于',num_2))

# pass 逻辑站位


# i = range(6,10)
# print(i)
# print(list(i))
#
# j = range(6,10,2)
# print(list(j))
# print(8 not in list(j))


# a = 0
# sumValue = 0
# while a<= 100:
#     if  bool(a % 2):
#         sumValue += a
#     else:
#        pass
#     a+=1
# print(sumValue)

# for i in range(100):
#    print(i)
#
#
# for _ in range(100):
#    print("1")



# for i in range(100,999):
#     result = 0
#     for n in str(i):
#          result+=int(n)*int(n)*int(n)
#     if result == i:
#         print(result)


# for i in range(0,3):
#     pwd = input("请输入密码:\n")
#     if pwd == '8888':
#         print("密码正确")
#         break
#     else:
#         print("密码错误")
# else:
#    print("系统关闭")

#
# for i in range(1,10):
#     for j in range(1,i+1):
#             print(i,"*",j,"=",j*i,end='\t')
#     print()


# 列表列表列表

# lst = [6,3,1,0,9]
# print(lst[::-1])
# print(lst[0:3:1])

# lst.append(90)
# print(lst)
#
# lst2 = ["a","b"]
# lst.append(lst2)
# print(lst)
#
# lst.insert(1,lst2)
# print(lst)
#
# lst3 = [1,2]
# lst[1:]=lst3
# print(lst)

# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)
#
# print('-----')
#
# newlst = sorted(lst)
# print(newlst)

# lst = [i*2 for i in range(1,6)]
# print(lst)


# scores ={'zhang':100,'li':200,'yu':98}
# print(scores)
# print(type(scores))
#
# student = dict(name='s',age=20)
# print(student)
#
# print(scores.get("zhang"))
# print(scores.get("luo",87))
#
# print('zhang' in scores)
# print('zhang1' not in scores)
# del scores['zhang']
# print(scores)
#
# scores['chen'] = 1000
# print(scores)
#
# print(scores.keys())
# print(list(scores.values()))
#
# for item in scores:
#     print(scores.get(item))

#
# items = ['123','456','789']
# prices = [1,2,3]
#
# d =  {item:price for item,price in zip(items,prices)}
# print(d)


# print(100/8)

# alist = []
# for i in range(1,11):
#     if (i % 2 == 0):
#         alist.append( i*i )
#
#  print(alist)

# 推导式
blist = [i*i for i in range(1,11) if (i%2) == 0]
print(blist)



# file1 = open('venv/name.txt', 'w')
# file1.write('诸葛亮')
# file1.close()
#
#
# file2 = open('name.txt')
# print(file2.read())
# file2.close()
#
# file3 = open('name.txt','a')
# file3.write('张三')
# file3.close()
#
# file4 =  open('name.txt')
# print(file4.readline())
# file4.close()

# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)
#     print("-----")


file6 = open('name.txt')
print("当文件指针的位置 %s" %file6.tell())
print("当前读取到第一个字符，字符内容是 %s" %file6.read(1))

# 第一个参数代表偏移位置，第二个参数 0 表示从文件开头偏移 1表示从当前位置偏移 2从文件结尾
file6.seek(5,0)
print("进行了seek操作")
print("当前文件指针的位置 %s" %file6.tell())
print("当前读取到第一个字符，字符内容是 %s" %file6.read(1))
print("当文件指针的位置 %s" %file6.tell())
file6.close()





