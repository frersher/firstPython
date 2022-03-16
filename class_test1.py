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
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def print_role(self):
        print("name is %s,hp is %s" %(self.name, self.hp))


user1 = Player('tom', 100)  # 类的实例化
user2 = Player('jerry', 90)
user1.print_role()
user2.print_role()
