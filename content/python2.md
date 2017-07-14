Title: 2. 打开python的正确姿势
Slug: zhengquedezishi
Date: 2017-07-09 19:11
Category: 编程
Tags: python
Author: 潘俊xi
Summary: 安装、开发、执行


安装:
在[1. hello python](http://localhost:8000/hello-python.html)中提到了环境用anaconda。
安装前需要确认一下目前已经安装的python有哪些。
windows在cmd里输入"where python", 如果发现已经有python安装了, 去系统的环境变量里把和python相关的路径从PATH里删除。
linux/mac在console里输入"which python", 一般都是系统自带的/usr/bin/python, 建议把该文件换一个文件名,
然后在安装好anaconda后用符号连接, 创建从"/usr/bin/python"指向"*/anaconda/bin/python"的
[符号链接](https://www.ibm.com/developerworks/cn/linux/l-cn-hardandsymb-links/index.html),
这一步操作后可以方便的允许你在hadoop环境中调用自定义的python环境, 如果只是用于python学习, 可以略过 <br>

在处理完已经存在的python环境后, 开始安装anaconda, 需要把anaconda的path添加到环境变量的path。
linux用户在指定安装路径的时候注意一下, 尽量不要用/root/anaconda这将会导致非root组用户无法使用anaconda版的python<br>

开发:
同样, 在[1. hello python](http://localhost:8000/hello-python.html)中提到了IDE, 用pycharm。
用这个的原因在于有专门的debugger(不用再花式print和pdb调试, 不过web程序有时候还是需要pdb的)、语法高亮和补全、方便的源码查看。
[最初的环境配置](https://jingyan.baidu.com/article/e6c8503c6268aae54f1a18eb.html)、[DEBUG模式](http://blog.csdn.net/chenggong2dm/article/details/9368641)、[技巧小本子](https://www.zhihu.com/question/37787004)

执行:
在玩IDE的时候应该已经尝试过运行程序了, 下面说一下在OS的命令行中, 如何执行python程序, 打开操作系统的命令行程序, cmd/console, 输入python回车, 进入的是anaconda python环境,
