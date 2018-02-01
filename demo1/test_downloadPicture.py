import requests
import os

url = "http://pic62.nipic.com/file/20150322/19858325_125956421000_2.jpg"
root = "/home/fireworm/IdeaProjects/python/python_crawler/demo1"
path = root + url.split("/")[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已保存")
except:
    print("爬取失败")