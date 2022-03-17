# 35 类与实例
# user1 = {"name": "tom", "hp": 100}
# user2 = {"name": "jerry", "hp": 80}
#
#
# def print_role(rolename):
#     print("name is %s,hp is %s" % (rolename['name'], rolename['hp']))
#
# print_role(user1)

# 面向过程更符合机器，面向对象更符合人的思维
class Player():  # 定义一个类
    def __init__(self, name, hp, occu):
        self.__name = name
        self.hp = hp
        self.occu = occu

    def print_role(self):
        print("name is %s,hp is %s, occu is %s" % (self.__name, self.hp, self.occu))

    def updateName(self,newname):
        self.__name = newname


# 36 类的继承
class Monster():
    '定义怪物的类'
    def __init__(self, hp = 100):
        self.hp = hp
    def run(self):
        print('移动到某个位置')

class Animals(Monster):
    '普通的怪物'
    def __init__(self, hp=10):
        self.hp = hp


class Boss(Monster):
    'Boss类怪物'
    pass

a1 = Monster(200)
print(a1.hp)
print(a1.run())

a2 = Animals()
print(a2.hp)
print(a2.run())


# user1 = Player('tom', 100, 'war')  # 类的实例化
# user2 = Player('jerry', 90, 'master')
# user1.print_role()
# user2.print_role()
#
# # 通过修改名称方法
# user1.updateName('zhangs')
# user1.print_role()
# # 如果变量用__修饰则为私有的
# user1.name = 'lis'
# user1.print_role()
