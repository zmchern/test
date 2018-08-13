#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'zm'

class Fibonacci(object):
    '''返回一个fibonacci数列'''
    def __init__(self):
        self.fList = [0,1] #设置初始列表
        self.main()

    def main(self):
        listLen = input('请输入fibonacci数列的长度（3-50）：')
        self.checkLen(listLen)
        while len(self.fList) <int(listLen):
            self.fList.append(self.fList[-1]+self.fList[-2])
            print('得到的fibonacci数列为:\n%s'%self.fList)

    def checkLen(self,lenth): #检查输入的数据是否符合要求
        lenList = map(str,range(3,51))
        if lenth in lenList:
            print(u'输入的长度符合标准，继续运行')
        else:
            print(u'只能输入3-50，太长了不是算不出，只是没必要')
            exit()

if __name__ == '__main__':
    f = Fibonacci()

