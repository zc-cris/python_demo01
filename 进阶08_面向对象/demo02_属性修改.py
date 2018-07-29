# zc-cris

class Car():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.price = 2000

    def descripe_info(self):
        return "this is %s, producted when %s, now it's price is %d" % (self.name, self.year, self.price)

    def update_price(self, price):
        if price < 2000:
            print("价格太低了")
        else:
            self.price = price


my_car = Car("宝马", 2018)
info = my_car.descripe_info()
print(info)  # this is 宝马, producted when 2018, now it's price is 2000
my_car.update_price(5000)
print(my_car.price)  # 5000
my_car.price = 666
print(my_car.price)  # 666   可以通过直接句点操作来修改实例的属性值，但是推荐使用方法来修改（类似java的setter方法），获取属性可以直接通过句点
