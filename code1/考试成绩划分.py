try:
    score=input('请输入考试成绩：')
    score=float(score)
    if score>=91:
        print('A')
    elif 81<= score <90:
        print('B')
    elif 71<= score <80:
        print('C')
    elif 61<= score <70:
        print('D')
    else:
        print('E')
except:
    print('输入的成绩是非数值型')

#实现一组数据的连加操作
vec = list( range(1,11) )#list创建列表
m=0
for i in vec:
    m+=i
print(m)

#实现一组数据的连乘操作
x = list( range(1,11))
n = 1
for i in x:
    n*=i
print(n)

#运用冒泡排序实现[1，2，6，0.3，2，0.5，-1，2，4]
vec=[1,2,5,0.3,2,0.5,-1,2,4]
for i in range(len(vec)):  #len()返回元素的个数
    for j in range(i):
        if vec[j] > vec[i]:
            vec[j],vec[i] = vec[i], vec[j]
print(vec)