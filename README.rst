地址行政区化和对比小工具
=====================
介绍
----
在Debian Linux系统上使用Python2.7编写的小工具，用来把确定但杂乱的地址整理成 省-市-区（县）-街道 的形式。并根据老师的要求，把这些地址和其他地址做比对，是否在同一省/市/区。

其实这个项目毫无意义，做自己的Github练手用吧


依赖库
----
- os
- openpyxl
- httplib2
- json
- platform

使用方法
----
把表格转换为xslx格式。

在global_list.py文件中添加百度地图APIkey

运行根目录下 start.py 文件

注意事项
----

- 因为HTTP请求的缘故，数据量大时程序会比较慢。请耐心等待。

联系我
----
- 网站： `@kdwycz <https://blog.kdwycz.com>`_
- github：`@kdwycz <https://github.com/kdwycz>`_
- email：kdwycz@gmail.com