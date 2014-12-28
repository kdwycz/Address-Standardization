#!/usr/bin/env python
# coding=utf-8

__author__ = 'kdwycz'

# APIKEY 请自行申请并替换下列字符串，可新增
# http://developer.baidu.com/map/index.php
KEY = (
	'1A4RCEBGsTTKngDpX6G62sca',
	'8UcQSlGy6FBQXZEfeV1QTNc6',
	'3fvsqvuoWOBIIAzUyw3KS6fK',
	'7wy6KxfMNhxtluBGGWVRlu8p',
	'VUrGoUHK9G7uttdfEkUQIgZK',
	'x65QkAbw3sh6EEbKHaanaetb',
)

APINUM = len(KEY)

NUM = 0

# 前三级行政区的标志
DIVISIONS = ('省','市','区','盟','旗','县')


#跳过对某一步查询的处理 True or False
STEP = {
	'IB' : True,
	'LG' : True,
	'LH' : True,
	'YH' : True,
}