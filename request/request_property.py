import requests
r = requests.get("http://www.baidu.com")
#1. r.status_code
print(r.status_code)
#2. r.encoding header中猜测出的编码方式
r.encoding = 'utf-8'
#3. r.text
print(r.text)
print(type(r))
#4. r.headers
print(r.headers)
#5. r.content
print(r.content)
#6. r.apparent_encoding 从内容分析编码方式
print(r.apparent_encoding)




















