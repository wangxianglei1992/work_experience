import requests #调用requests库
from bs4 import BeautifulSoup

#获取网页源代码，得到的res是Response对象
res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/')
print('响应状态码:',res.status_code) #检查请求是否正确响应

res.encoding = 'utf-8'

soup = BeautifulSoup( res.text,'html.parser')
print(type(soup)) #查看soup的类型

items = soup.find_all(class_="comment-content") #使用find()方法提取首个<div>元素，并放到变量item里。
print(type(items)) 

for item in items:
    comments=item.find('p')
    print(type(comments))
    print(comments)
    print(comments.text,'\n')
    #创建一个名为《三国演义》的txt文档，指针放在文件末尾，追加内容
    k = open('评论.txt','a+')
    k.write(comments.text)
    k.close

'''
for item in item_all:
 
    kind = item.find('h2') # 在列表中的每个元素里，匹配标签<h2>提取出数据
    print(kind.text,'\n')
    print(kind.text,'\n')

    title = item.find(class_='title') # 在列表中的每个元素里，匹配标签<h2>提取出数据
    
    print(title,'\n')
    print(type(title),'\n')

    print(title.text,'\n')
    print(type(title.text),'\n')

    print(title['href'],'\n')
    print(type(title['href']),'\n')

    title = item.find(class_='title') #在列表中的每个元素里，匹配属性class_='title'提取出数据
    brief = item.find(class_='info') #在列表中的每个元素里，匹配属性class_='info'提取出数据
    print(kind,'\n',title,'\n',brief) # 打印提取出的数据
    print(type(kind),type(title),type(brief)) # 打印提取出的数据类型

'''


