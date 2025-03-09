import re       #导入re模块，相当于库
#读取文本文件

f=open('walden.txt',mode='r')   #注意将文件放在同一工程文件目录下  mode-读取模式
text=f.read()                   #读取文件数据
f.close()                       #关闭文件

# f=open('walden.txt',mode='r')   #注意将文件放在同一工程文件目录下  mode-读取模式
# text=f.readline()  #以列表的形式读取文件

#去除多余符号
lyric = txt.lower()                                       #将大写字母转化为小写字母
lyric_new = re.sub('[,.:"\'?\n;-]','',lyric)  #去除多余标点符号，注意转义字符‘前用\
#单词分割
words=lyric_new.split()
#词频设计
word_freq={}                                #构建一个空字典，用于记录各单词的词频
for word in words:
    if word not in word_freq.keys():        #判断当前访问单词是否在词典中
        word_freq[word]=1                   #若不在则以该单词为键创建一个键值，且赋值为1
    else:
        word_freq[word]+=1                  #若在则将该单词对应的值加1
#排序

result=sorted(word_freq.item(),key=lambda x: x[1],reverse=True) #lambda x: x[1]带表只排序构建对的第二个，即每个单词的频次
#写出结果
result_string=str(result)   #将结果转化问字符串形式

with open('word_freq.txt',mode='w') as f:   #使用with打开文件在程序结束时会自动关闭文件，不用担心因为报错导致的文件一直被占用
    f.write(result_string)