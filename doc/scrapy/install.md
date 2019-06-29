# Scrapy 安装

报错
----
* 问题：windows安装Scrapy报错
```
building 'twisted.test.raiser' extension
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools"
```
解决：
  [twisted.whl文件下载](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)<br>
```
pip install Twisted-19.2.1-cp37-cp37m-win_amd64.whl
pip install Scrapy
```