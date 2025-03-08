#使用def定义函数
def def_sum(x,y):
    z= x + y
    print(z)
    return z
def_sum(x= 3, y= 4)


vec=[1,2,3,4,5,6,7,8,9]
def def_mean(x):
    m = 0
    for i in x:
        m+=i
    return m/len(x)

print(def_mean(vec))


#使用lambda定义【匿名】函数
y = lambda x: x ** 2
print(y(10))

# 使用def和lambda定义函数的区别
# def常用于复杂函数的定义
# lambda常用于定义简短的匿名函数

pi = 3.1415926