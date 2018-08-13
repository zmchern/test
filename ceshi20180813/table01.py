#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'zmchern'

class PrintTable(object):
    def __init__(self):
        print(u"开始打印9*9的乘法表格")
        self.print99()

    def print99(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print('%d×%d=%2s'%(j,i,i*j))
            print('\n')

if __name__ == '__main__':
    pt = PrintTable()