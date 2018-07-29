# zc-cris

class Dog():
    '''python中创建一个类模拟狗'''

    def __init__(self, name, age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " is now rolling over")


my_dog = Dog("cris", 12)
# 访问实例中的属性
print(my_dog.name)
# 调用实例的方法
my_dog.sit()
my_dog.roll_over()
