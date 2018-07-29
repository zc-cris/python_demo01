# zc-cris


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + " is eatting！")

    def sleep(self):
        print(self.name + " is sleeping")


class Computer():
    def __init__(self, name='惠普'):
        self.name = name

    def descripe(self):
        print("电脑的名字默认是:%s" % self.name)


class Student(Person):

    def __init__(self, name, age, computer=Computer(), score=0):
        super().__init__(name, age)
        self.score = score
        self.computer = computer

    def exam(self):
        print("学生的成绩默认是%s" % self.score)

    def sleep(self):
        print("中国学生睡眠严重不足")


student = Student('cris', 12)
student.eat()  # crisis eatting！
print(student.name)  # cris
student.exam()  # 学生的成绩默认是0
student.sleep()  # 中国学生睡眠严重不足
student.computer.descripe()
