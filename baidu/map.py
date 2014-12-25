#!/usr/bin/env python
# coding=utf-8
__author__ = 'kdwycz'

import json
import httplib2

S11 = 'http://api.map.baidu.com/place/v2/search?q='
S12 = '&region=中国&output=json&ak='
S21 = 'http://api.map.baidu.com/geocoder/v2/?ak='
S22 = '&location='
S23 = '&output=json&pois=0'
h =httplib2.Http()

def findxy(ss,APIKEY):
    url = S11 + ss + S12 + APIKEY
    resp, content = h.request(url)
    data = json.loads(content)
    x = data[u'results'][0][u'location'][u'lat']
    y = data[u'results'][0][u'location'][u'lng']
    return x,y

def finddir(xy,APIKEY):
    url = S21 + APIKEY + S22 + str(xy[0]) + ',' + str(xy[1]) + S23
    resp, content = h.request(url)
    data = json.loads(content)
    ddict = {}
    ddict['province'] = data[u'result'][u'addressComponent'][u'province']
    ddict['city'] = data[u'result'][u'addressComponent'][u'city']
    ddict['district'] = data[u'result'][u'addressComponent'][u'district']
 #  ddict['street'] = data[u'result'][u'addressComponent'][u'street']
 #  ddict['number'] = data[u'result'][u'addressComponent'][u'street_number']
    return ddict

if __name__ == '__main__':
    print'search 江西师范大学瑶湖校区'
    ss = '江西师范大学瑶湖校区'
    xy = findxy(ss)
    dd = finddir(xy)
    print(dd['province'])
    print(dd['city'])
    print(dd['district'])
 #  print(dd['street'])

