#!/usr/bin/env python
# coding=utf-8

__author__ = 'kdwycz'

import os
import json
import codecs
from global_list import *
import baidu.map as baidu

def read_file(files):
    """读取文件函数：
    参数：文件路径和文件名（相对于input目录）
    返回：一个列表，列表的每个元素代表输入文件的一行，
    是一个元组，有两个字符串。
    """
    try:
    	data = []
    	fileread = open('./input/' + files, 'r')
    except IOError as err:
    	print('File Error:'+str(err))
    	return data
    for line in fileread.readlines():
        data1 = line.split('\t')[0]
        data2 = line.split('\t')[1]
        data2 = data2.strip()
        ttuple = (data1, data2)
        data.append(ttuple)
    fileread.close()
    return data

def analyse(address):
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
            NUM += 1
    return (flag,ddict)

def save_dict(ddict, name):
    fw = codecs.open('./temp/' + name,'w','utf-8')
    strdict = json.dumps(ddict, encoding="utf-8")
    fw.write(strdict)
    fw.close()

def load_dict(name):
    strdict = open('./temp/' + name).read()
    strdict  = json.loads(strdict)
    ddict = {}
    for (key,value) in strdict.items():
        ddict[int(key)] = value
    return ddict

def compare(num, dict1, dict2, fw):
    """地址比较函数
    输入：地址一的key 地址一 地址库 输出文件对象
    """
    if num not in dict2:
        fw.write('no number\n')
    elif dict1[u'province'] != dict2[num][u'province']:
        fw.write('4\n')
    elif dict1[u'city'] != dict2[num][u'city']:
        fw.write('3\n')
    elif dict1[u'district'] != dict2[num][u'district']:
        fw.write('2\n')
    else:
        fw.write('1\n')

def comp_lh(num, addr, fw, char):
    addr = addr + DIVISIONS[1]
    ddict = analyse(addr)
    if ddict[0]:
        ddict = ddict[1]
        if num not in rootdict:
            fw.write('no number')
            fw.write(char)
        elif ddict[u'province'] != rootdict[num][u'province']:
            fw.write('4')
            fw.write(char)
        elif ddict[u'city'] != rootdict[num][u'city']:
            fw.write('3')
            fw.write(char)
        elif ddict[u'district'] != rootdict[num][u'district']:
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
    if not os.path.exists('temp'):
        os.mkdir('temp')

    if not os.path.isfile('./temp/rootdict'):
        print(u'读取主地址并进行标准化输出')
        data = read_file('root.txt')
        fw = codecs.open('./output/root.txt','w','utf-8')
        rootdict = {}
        for item in data:
            num = int(item[0])
            addr = item[1]
            ddict = analyse(addr)
            if ddict[0]:
                ddict = ddict[1]
                rootdict[num] = ddict
                fw.write(str(num)); fw.write('\t'); fw.write(ddict['province'])
                fw.write(ddict['city']); fw.write(ddict['district']); fw.write('\n')
            else:
                fw.write('error\n')
        fw.close()
        save_dict(rootdict,'rootdict')
    else:
        print(u'从本地读取主地址')
        rootdict = load_dict('rootdict')

    if STEP['IB']:
        print(u'IB表输入和主地址进行比对')
        data = read_file('IB.txt')
        fw = codecs.open('./output/IB.txt','w','utf-8')
        tw = codecs.open('./temp/IB','w','utf-8')
        for item in data:
            num = int(item[0])
            addr = item[1]
            ddict = analyse(addr)
            if ddict[0]:
                ddict = ddict[1]
                tw.write(str(num)); tw.write('\t'); tw.write(ddict['province'])
                tw.write(ddict['city']); tw.write(ddict['district']); tw.write('\n')
                compare(num,ddict,rootdict,fw)
            else:
                fw.write('error\n')
                tw.write('error\n')
        fw.close()
        tw.close()

    if STEP['YH']:
        print(u'YH表输入和主地址进行比对')
        data = read_file('YH.txt')
        fw = codecs.open('./output/YH.txt','w','utf-8')
        tw = codecs.open('./temp/YH','w','utf-8')
        for item in data:
            num = int(item[0])
            addr = item[1]
            ddict = analyse(addr)
            if ddict[0]:
                ddict = ddict[1]
                tw.write(str(num)); tw.write('\t'); tw.write(ddict['province'])
                tw.write(ddict['city']); tw.write(ddict['district']); tw.write('\n')
                compare(num,ddict,rootdict,fw)
            else:
                fw.write('error\n')
                tw.write('error\n')
        fw.close()
        tw.close()

    if not os.path.isfile('./temp/hoteldict'):
        print(u'读取旅馆地址并进行标准化输出')
        data = read_file('hotel.txt')
        fw = codecs.open('./output/hotel.txt','w','utf-8')
        hoteldict = {}
        for item in data:
            num = int(item[0])
            addr = item[1]
            ddict = analyse(addr)
            if ddict[0]:
                ddict = ddict[1]
                hoteldict[num] = ddict
                fw.write(str(num)); fw.write('\t'); fw.write(ddict['province'])
                fw.write(ddict['city']); fw.write(ddict['district']); fw.write('\n')
            else:
                fw.write('error\n')
        fw.close()
        save_dict(hoteldict,'hoteldict')
    else:
        print(u'从本地读取旅馆地址')
        hoteldict = load_dict('hoteldict')

    if STEP['LG']:
        print(u'读取LG表并进行比对')
        data = read_file('LG.txt')
        fw = codecs.open('./output/LG.txt','w','utf-8')
        for item in data:
            num1 = int(item[0])
            num2 = int(item[1])
            if num1 not in rootdict or num2 not in hoteldict:
                fw.write('error\n')
            elif rootdict[num1][u'province'] != hoteldict[num2][u'province']:
                fw.write('4\n')
            elif rootdict[num1][u'city'] != hoteldict[num2][u'city']:
                fw.write('3\n')
            elif rootdict[num1][u'district'] != hoteldict[num2][u'district']:
                fw.write('2\n')
            else:
                fw.write('1\n')
        fw.close()

    if STEP['LH']:
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
    
