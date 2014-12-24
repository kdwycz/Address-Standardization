#!/usr/bin/env python
# coding=utf-8

__author__ = 'kdwycz'

import baidu.map as baidu
import codecs

#读取主地址并进行标准化输出
fr = open('./input/root.txt','r')
fw = codecs.open('./output/root.txt','w','utf-8')
rootdict = {}
for line in fr.readlines():
    num = int(line.split('\t')[0])
    data = line.split('\t')[1]
    data = data.strip()
    xy = baidu.findxy(data)
    dd = baidu.finddir(xy)
    rootdict[num] = dd
    fw.write(str(num)); fw.write('\t'); fw.write(dd['province']); fw.write(dd['city']); fw.write(dd['district']); fw.write('\n')
fr.close()
fw.close()

#IB表输入和主地址进行比对
fr = open('./input/IB.txt','r')
fw = codecs.open('./output/IB.txt','w','utf-8')
for line in fr.readlines():
    num = int(line.split('\t')[0])
    data = line.split('\t')[1]
    data = data.strip()
    xy = baidu.findxy(data)
    dd = baidu.finddir(xy)
    if num not in rootdict:
        fw.write('error\n')
    elif dd['province'] != rootdict[num]['province']:
        fw.write('4\n')
    elif dd['city'] != rootdict[num]['city']:
        fw.write('3\n')
    elif dd['district'] != rootdict[num]['district']:
        fw.write('2\n')
    else:
        fw.write('1\n')
fr.close()
fw.close()

#YH表输入和主地址进行比对
fr = open('./input/YH.txt','r')
fw = codecs.open('./output/YH.txt','w','utf-8')
for line in fr.readlines():
    num = int(line.split('\t')[0])
    data = line.split('\t')[1]
    data = data.strip()
    xy = baidu.findxy(data)
    dd = baidu.finddir(xy)
    if num not in rootdict:
        fw.write('error\n')
    elif dd['province'] != rootdict[num]['province']:
        fw.write('4\n')
    elif dd['city'] != rootdict[num]['city']:
        fw.write('3\n')
    elif dd['district'] != rootdict[num]['district']:
        fw.write('2\n')
    else:
        fw.write('1\n')
fr.close()
fw.close()

#读取旅馆地址并进行标准化输出
fr = open('./input/hotel.txt','r')
fw = codecs.open('./output/hotel.txt','w','utf-8')
hoteldict = {}
for line in fr.readlines():
    num = int(line.split('\t')[0])
    data = line.split('\t')[1]
    data = data.strip()
    xy = baidu.findxy(data)
    dd = baidu.finddir(xy)
    hoteldict[num] = dd
    fw.write(str(num)); fw.write('\t'); fw.write(dd['province']); fw.write(dd['city']); fw.write(dd['district']); fw.write('\n')
fr.close()
fw.close()

#读取LG表并进行比对
fr = open('./input/LG.txt','r')
fw = codecs.open('./output/LG.txt','w','utf-8')
for line in fr.readlines():
    num1 = int(line.split('\t')[0])
    data = line.split('\t')[1]
    data = data.strip()
    num2 = int(data)
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
fr.close()
fw.close()

