#!/usr/bin/env python
# coding=utf-8

__author__ = 'kdwycz'

import os
import codecs
from global_list import *
import baidu.map as baidu

def read_file(files):
    """读取文件函数：
    参数：文件路径和文件名（相对于input目录）
    返回：一个列表，列表的每个元素代表输入文件的一行，
    是一个元组，有两个字符串。
    """
    fileread = open('./input/' + files, 'r')
    data = []
    for line in fileread.readlines():
        data1 = line.split('\t')[0]
        data2 = line.split('\t')[1]
        data2 = data2.strip()
        ttuple = (data1, data2)
        data.append(ttuple)
    fileread.close()
    return data


def analyse(address,apikey):
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
        xy = baidu.findxy(address, apikey)
        if xy == (0,0):
            flag = False
        else:
            ddict = baidu.finddir(xy, apikey)
    return (flag,ddict)


def compare(num, dict1, dict2, fw):
    """地址比较函数
    输入：地址一的key 地址一 地址库 输出文件对象
    """
    if num not in dict2:
        fw.write('no number\n')
    elif dict1['province'] != dict2[num]['province']:
        fw.write('4\n')
    elif dict1['city'] != dict2[num]['city']:
        fw.write('3\n')
    elif dict1['district'] != dict2[num]['district']:
        fw.write('2\n')
    else:
        fw.write('1\n')

def comp_lh(num, addr, fw, char):
    addr = addr + DIVISIONS[1]
    ddict = analyse(addr,KEY[APINUM[4]])
    if ddict[0]:
        ddict = ddict[1]
        if num not in rootdict:
            fw.write('no number')
            fw.write(char)
        elif ddict['province'] != rootdict[num]['province']:
            fw.write('4')
            fw.write(char)
        elif ddict['city'] != rootdict[num]['city']:
            fw.write('3')
            fw.write(char)
        elif ddict['district'] != rootdict[num]['district']:
            fw.write('2')
            fw.write(char)
        else:
            fw.write('1')
            fw.write(char)
    else:
        fw.write('error')
        fw.write(char)

if __name__ == '__main__':

    if not os.path.exists('output'):
        os.mkdir('output')

    print(u'读取主地址并进行标准化输出')
    data = read_file('root.txt')
    fw = codecs.open('./output/root.txt','w','utf-8')
    rootdict = {}
    for item in data:
        num = int(item[0])
        addr = item[1]
        ddict = analyse(addr,KEY[APINUM[0]])
        if ddict[0]:
            ddict = ddict[1]
            rootdict[num] = ddict
            fw.write(str(num)); fw.write('\t'); fw.write(ddict['province'])
            fw.write(ddict['city']); fw.write(ddict['district']); fw.write('\n')
        else:
            fw.write('error\n')
    fw.close()
    

    print(u'IB表输入和主地址进行比对')
    data = read_file('IB.txt')
    fw = codecs.open('./output/IB.txt','w','utf-8')
    for item in data:
        num = int(item[0])
        addr = item[1]
        ddict = analyse(addr,KEY[APINUM[1]])
        if ddict[0]:
            ddict = ddict[1]
            compare(num,ddict,rootdict,fw)
        else:
            fw.write('error\n')
    fw.close()


    print(u'YH表输入和主地址进行比对')
    data = read_file('YH.txt')
    fw = codecs.open('./output/YH.txt','w','utf-8')
    for item in data:
        num = int(item[0])
        addr = item[1]
        ddict = analyse(addr,KEY[APINUM[2]])
        if ddict[0]:
            ddict = ddict[1]
            compare(num,ddict,rootdict,fw)
        else:
            fw.write('error\n')
    fw.close()
    
    print(u'读取旅馆地址并进行标准化输出')
    data = read_file('hotel.txt')
    fw = codecs.open('./output/hotel.txt','w','utf-8')
    hoteldict = {}
    for item in data:
        num = int(item[0])
        addr = item[1]
        ddict = analyse(addr,KEY[APINUM[3]])
        if ddict[0]:
            ddict = ddict[1]
            hoteldict[num] = ddict
            fw.write(str(num)); fw.write('\t'); fw.write(ddict['province'])
            fw.write(ddict['city']); fw.write(ddict['district']); fw.write('\n')
        else:
            fw.write('error\n')
    fw.close()

    print(u'读取LG表并进行比对')
    data = read_file('LG.txt')
    fw = codecs.open('./output/LG.txt','w','utf-8')
    for item in data:
        num1 = int(item[0])
        num2 = int(item[1])
        if num1 not in rootdict or num2 not in hoteldict:
            fw.write('error\n')
        elif rootdict[num1]['province'] != hoteldict[num2]['province']:
            fw.write('4\n')
        elif rootdict[num1]['city'] != hoteldict[num2]['city']:
            fw.write('3\n')
        elif rootdict[num1]['district'] != hoteldict[num2]['district']:
            fw.write('2\n')
        else:
            fw.write('1\n')
    fw.close()

    print(u'LH表输入和主地址进行比对')
    fr = open('./input/LH.txt', 'r')
    fw = codecs.open('./output/LH.txt','w','utf-8')
    for line in fr.readlines():
        num1 = int(line.split('\t')[0])
        addr1 = line.split('\t')[1]
        addr2 = line.split('\t')[2]
        addr2 = addr2.strip()
        comp_lh(num1, addr1, fw, '\t')
        comp_lh(num1, addr2, fw, '\n')
    fr.close()
    fw.close()

    print(u'全部完成')
    
