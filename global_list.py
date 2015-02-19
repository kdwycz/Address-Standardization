#!/usr/bin/env python
# coding=utf-8

__author__ = 'kdwycz'

# APIKEY 请自行申请并替换下列字符串，可新增
# http://developer.baidu.com/map/index.php
KEY = (
	u'1A4RCEBGsTTKngDpX6G62sca',
	u'8UcQSlGy6FBQXZEfeV1QTNc6',
	u'3fvsqvuoWOBIIAzUyw3KS6fK',
	u'7wy6KxfMNhxtluBGGWVRlu8p',
	u'VUrGoUHK9G7uttdfEkUQIgZK',
	u'x65QkAbw3sh6EEbKHaanaetb',
)

APINUM = len(KEY)

NUM = 0

# 前三级行政区的标志
DIVISIONS = (u'省',u'市',u'区',u'盟',u'旗',u'县')

ROOTNAME = u'主地址'
HOTELNAME = u'旅馆代码'

ROOTSET = ['IB','YH','LH']
MIXSET = 'LG'

#Linux为0;windows为1.程序会自行判断.影响表格行列起始值
#OS = 0