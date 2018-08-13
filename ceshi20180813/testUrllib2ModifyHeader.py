#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import urllib.request
import userAgents
'''userAgents.py是个自定义的模块，位置处于当前目录下 '''

class UrllibModifyHeader(object):
	'''使用urllib模块修改header '''
	def __init__(self):
		#这个是PC + IE 的User-Agent
		PIUA = userAgents.pcUserAgent.get('IE 9.0')
		#这个是Mobile + UC的User-Agent
		MUUA = userAgents.mobileUserAgent.get('UC standard')
		#测试用的网站选择的是有道翻译
		self.url = 'http://www.baidu.com'

		self.useUserAgent(PIUA,1)
		self.useUserAgent(MUUA,2)

	def useUserAgent(self,userAgent,name):
		req = urllib.request(self.url)
		req.add_header(userAgent.split(':')[0],userAgent.split(':')[1])
		response = urllib.request.urlopen(req)
		fileName = str(name) + '.html'
		with open(fileName,'a') as fp:
			fp.write("%s\n\n" %userAgent)
			fp.write(response.read())

if __name__ == '__main__':
	umh = UrllibModifyHeader()
