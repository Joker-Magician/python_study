class Human:
    def __init__(self, age , gender):
        self.age=age            #类的属性
        self.gender=gender

    def sqrt(self,x):
        return x**2


zhangfei = Human(age=23,gender='男')   #类的实例化，得到一个对象
print(zhangfei.age)  #对象的属性
print(zhangfei.sqrt(10) )  #调用对象的方法

all_in_list=[0.2,0.25]
all_in_list.append(3.56)  #这个对象可以调用方法append追加元素，但Human不可以
print(all_in_list)


#相当于结构体
