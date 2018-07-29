# zc-cris

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + " is eatting~~~")


class Package():
    def __init__(self, price, name='adidas'):
        self.price = price
        self.name = name

    def descripe(self):
        return "这是个%s 的书包，价格：%d" % (self.name, self.price)


class Student(Person):
    def __init__(self, name, age, height, package=Package(100)):
        super().__init__(name, age)
        self.height = height
        self.package = package

    def descripe(self):
        print("我叫%s, 今年%d岁了，身高%d, 我的书包的详细信息是：%s" % (self.name, self.age, self.height, self.package.descripe()))
