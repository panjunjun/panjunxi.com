Title: 4. 文件路径的介绍
Slug: file-path
Date: 2017-07-12 14:50
Category: 编程
Tags: python
Author: 潘俊xi
Summary: python对操作系统文件路径的介绍


python是一个可以跨操作系统的语言, 如果有人和我一样蛋疼的话: 公司用mac, 家里用windows, 服务器用linux。那一定会碰到文件路径引起的问题。<br>
正确操作文件路径的包是标准库os <br>


获取当前文件的绝对路径file-path.py:
```python
import os
print(os.path.abspath(__file__))
```
在Mac中执行:
```Mac
python /Users/panjunxi/PycharmProjects/Lab/blog/file-path.py
/Users/panjunxi/PycharmProjects/Lab/blog/file-path.py
```

执行的命令是用python这个可执行程序, 带入一个文件名/路径的参数。
执行的结果是打印file-path.py这个文件的绝对路径, 代码中出现的"\__file__"则是python内置的[魔术方法](http://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/a-guide-to-pythons-magic-methods.html), 通过它能够获取模块的文件信息,
而"os.path.abspath"这个方法则返回的是一个文件路径的字符串, 会根据你的操作系统调整分隔符, linux/mac为"/", windows为"\"
这样就可以避免对路径的[硬编码](http://baike.baidu.com/item/%E7%A1%AC%E7%BC%96%E7%A0%81), 能增加代码的可移植性 <br>

更多的os库的方法可以通过查阅[python官方文档](https://docs.python.org/3/library/os.html)、源代码、培训课程(例如[极客学院](http://wiki.jikexueyuan.com/project/explore-python/File-Directory/os.html))、其他博客等, 还是建议科学上网, Google一下<br>

