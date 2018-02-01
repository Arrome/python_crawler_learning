import requests
kv = {'wd':'python'}
url = "https://www.baidu.com"
try:
    #百度的关键词接口：http://www.baidu.com/s?wd=keyword
    #360的关键词接口：http://www.so.com/s?q=keyword
    r = requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
    print(r.request.headers)
except:
    print("爬取失败")