#!/usr/bin/env python
# coding=utf-8

__author__ = 'kdwycz'

import os
from openpyxl import load_workbook
from global_list import *
import baidu.map as baidu
import platform

def Analyse(address):
    """分析地区名是否合法函数：
    输入：地址字符串,百度APIKEY
    返回：一个元组，第一个元素是True/False。如果为True，
    第二个元素是一个字典。表示地区的省市县
    """
    flag = False
    for divisions in DIVISIONS:
        if divisions in address:
            flag = True
            break
    ddict = {}
    if flag:
        global NUM
        xy = baidu.findxy(address, KEY[NUM % APINUM])
        NUM += 1
        if xy == (0,0):
            flag = False
        else:
            ddict = baidu.finddir(xy, KEY[NUM % APINUM])
            if ddict[u'province'] == u'error':
                flag = False
            NUM += 1
    return (flag,ddict)

def CreateDict(sheetname,maindict):
    error = 0
    inws = inwb.get_sheet_by_name(sheetname)
    sheetrow = inws.get_highest_row()
    sheetcol = inws.get_highest_column()
    for i in range(1+OS,sheetrow+OS):
        num = inws.cell(row=i,column=0+OS).value
        address = inws.cell(row=i,column=1+OS).value
        flag = True
        if num and address:
            ddict = Analyse(address)
            if ddict[0]:
                ddict = ddict[1]
                maindict[num] = ddict
                address = ddict['province'] + ddict['city'] + ddict['district']
                inws.cell(row=i,column=sheetcol+OS).value = address
            else:
                flag = False
        else:
            flag = False
        if not flag:
            inws.cell(row=i,column=sheetcol+OS).value = 'Error'
            error += 1
    return error

def CheckDict(sheetname,maindict):
    error = 0
    inws = inwb.get_sheet_by_name(sheetname)
    sheetrow = inws.get_highest_row()
    sheetcol = inws.get_highest_column()
    for i in range(1+OS,sheetrow+OS):
        num = inws.cell(row=i,column=0+OS).value
        for j in xrange(1+OS,sheetcol+OS):
            address = inws.cell(row=i,column=j).value
            flag = True
            if num and address:
                if sheetname == 'LH':
                    address += u'市'
                ddict = Analyse(address)
                if ddict[0]:
                    ddict = ddict[1]
                    if num not in maindict:
                        flag = False
                    elif ddict['province'] != maindict[num]['province']:
                        result = 4
                    elif ddict['city'] != maindict[num]['city']:
                        result = 3
                    elif ddict['district'] != maindict[num]['district']:
                        result = 2
                    else:
                        result = 1
                else:
                    flag = False
            else:
                flag = False
            if not flag:
                result = 'error'
                error += 1
            inws.cell(row=i,column=sheetcol+j-1).value = result
    return error

def CheckDoubleDict():
    error = 0
    inws = inwb.get_sheet_by_name(MIXSET)
    sheetrow = inws.get_highest_row()
    sheetcol = inws.get_highest_column()
    for i in range(1+OS,sheetrow+OS):
        num1 = inws.cell(row=i,column=0+OS).value
        num2 = inws.cell(row=i,column=1+OS).value
        flag = True
        if num1 and num2 and (num1 in rootdict) and (num2 in hoteldict):
            if rootdict[num1]['province'] != hoteldict[num2]['province']:
                result = 4
            elif rootdict[num1]['city'] != hoteldict[num2]['city']:
                result = 3
            elif rootdict[num1]['district'] != hoteldict[num2]['district']:
                result = 2
            else:
                result = 1
        else:
            flag = False
        if not flag:
            result = 'error'
            error += 1
        inws.cell(row=i,column=2+OS).value = result
    return error


if __name__ == '__main__':

    print(u'程序开始运行...')

    sysstr = platform.system()
    if sysstr == "Windows":
        OS = 1

    if not os.path.exists('output'):
        os.mkdir('output')

    try:
        inwb = load_workbook('./input/data.xlsx')
    except:
        print (u'文件读取错误')
    else:
	    rootdict = {}
	    hoteldict = {}

	    error = CreateDict(ROOTNAME,rootdict)
	    print (u"读取主地址并进行标准化输出,出现错误数: %d" %error)
	    
	    error = CreateDict(HOTELNAME,hoteldict)
	    print (u"读取旅馆地址并进行标准化输出,出现错误数: %d" %error)

	    for item in ROOTSET:
	        error = CheckDict(item,rootdict)
	        print (u"读取%s表并进行比对,出现错误数: %d" %(item,error))
	    
	    error = CheckDoubleDict()
	    print (u"读取%s表并进行比对,出现错误数: %d" %(MIXSET,error))
	    
	    inwb.save('./output/tst.xlsx')
	    print (u'全部完成')
