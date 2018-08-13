#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

def clear():
    '''该函数用于清屏'''
    print(u'内容较多，显示3秒后翻页')
    time.sleep(3)
    OS = platform.system() #读取系统
    if (OS == u'Windows'):
        os.system('cls')
    else:
        os.system('clear')
def linkBaidu():
    url = 'https://www.baidu.com'
    try:
        response = urllib.request.urlopen(url,timeout = 3)
        print(type(response))
    except urllib.request.URLError:
        print(u'网络地址错误')
        exit()
    with open('./baidu.txt','w') as fp:
        fp.write(response.read().decode('utf-8'))
    print(u'获取url信息，response.geturl() \n:%s'%response.geturl())
    print(u'获取返回代码，response.getcode() \n:%s'%response.getcode())
    print(u'获取返回代码，response.status() \n:%s'%response.status())
    print(u'获取返回信息，response.info() \n:%s'%response.info())
    print(u'获取的网页内容已存入当前目录的baidu.txt中，请自行查看')

if __name__ == '__main__':
    linkBaidu()