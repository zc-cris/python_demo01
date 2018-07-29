# zc-cris

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + " is eatting")

    def sleep(self):
        if self.age > 50:
            print(self.name + " need more rest")
        else:
            print(self.name + " can sleep less")
