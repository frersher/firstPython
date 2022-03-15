# def func (a,b,c):
#     print('a=%s' %a)
#     print('b=%s' %b)
#     print('c=%s' %c)
#
# func(c=1,b=3,a=8)


# 取函数的个数
# def howlong(first,*others):
#     print(1+len(others))
#
# howlong(1,3,4,5,6)


# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))


# for i in range(10,20,2):
#     print(i)


# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
#
#
# for i in frange(10, 20, 0.5):
#     print(i)

# lamda表达式
# lambda : True
#
# def add(x,y):return x+y
#
# lambda x,y:x+y

# 函数
# a = [1, 2, 3, 4, 5, 6, 7]
# b = list(filter(lambda x:x>2,a))
# print(b)

# a = [1, 2, 3]
# b = [2, 3, 4]
# c = list(map(lambda x, y: x+y, a, b))
# print(c)


# from functools import reduce
# a = reduce(lambda x, y: x+y, [1, 2, 3], 1)
# print(a)


# for i in zip((1, 2, 3), (4, 5, 6)):
#     print(i)


# dicta = {'a': 'aa', 'b': 'bb'}
# dictb = zip(dicta.values(),dicta.keys())
# print(dict(dictb))


# 闭包
# def sum(a):
#     def add(b):
#         return a + b
#
#     return add
#
# num1 = sum(2)
# print(num1(1))


# def counter():
#     cnt = [0]
#     def add_one():
#         cnt[0] += 1
#         return cnt[0]
#
#     return add_one
#
# num1 =  counter(5)
#
# print(num1())
# print(num1())
# print(num1())
# print(num1())


# 装饰器定义

# import time
#
# def timer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print('函数运行了 %s s' % (stop_time - start_time))
#     return wrapper
#
#
# @timer
# def i_can_sleep():
#     time.sleep(3)
#
# i_can_sleep()


def tips(func):
    def nei(a,b):
        print("start")
        func(a,b)
        print("stop")

    return nei


@tips
def add(a,b):
    print(a+b)

@tips
def sub(a,b):
    print(a-b)

print(add(1,2))
print(sub(9,5))