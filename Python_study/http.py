#引入requests库
import requests

#发送请求，并把响应结果赋值在变量res上
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
res1 = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')

#打印变量res的响应状态码，以检查请求是否成功
print(res.status_code)
print(res1.status_code)

#定义Reponse对象的编码为utf-8
res.encoding = 'utf-8'
#把Response对象的内容以字符串的形式返回
novel = res.text

#创建一个名为《三国演义》的txt文档，指针放在文件末尾，追加内容
k = open('三国演义.txt','a+')
k.write(novel)
k.close

#把Reponse对象的内容以二进制数据的形式返回
pic = res1.content

#新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
#图片内容需要以二进制wb读写
photo = open('ppt.jpg','wb')
photo.write(pic)
photo.close()