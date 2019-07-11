import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
res1 = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')

pic = res1.content

photo = open('ppt.jpg','wb')
photo.write(pic)
photo.close()

print(res.status_code)
print(res1.status_code)