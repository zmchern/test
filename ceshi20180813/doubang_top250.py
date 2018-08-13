# -*- coding:utf-8 -*-
__author__ = 'Jz'
import urllib.request
from urllib import error
import re
import sys
import importlib


class MovieTop250:
    def __init__(self):
        # 设置默认编码格式为utf-8
        importlib.reload(sys)
        #sys.setdefaultencoding('utf-8')
        self.start = 0
        self.param = '&filter=&type='
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
        self.movieList = []
        self.filePath = 'D:/DoubanTop250.txt'

    def getPage(self):
        try:
            URL = 'http://movie.douban.com/top250?start=' + str(self.start)
            response = urllib.request.urlopen(url=URL)
            page = response.read().decode('utf-8')
            pageNum = (self.start + 25) / 25
            print('正在抓取第' + str(pageNum) + '页数据...')
            self.start += 25
            return page
        except error.URLError as e:
            if hasattr(e, 'reason'):
                print('抓取失败，具体原因：', e.reason)

    def getMovie(self):
        pattern = re.compile(u'<li>.*?<div.*?class="item">.*?<div.*?class="pic">.*?'
                             + u'<em.*?class="">(.*?)</em>.*?'  # 排名
                             + u'<div.*?class="info">.*?<span.*?class="title">(.*?)</span>.*?'  # 电影名
                             + u'<span.*?class="other">&nbsp;/&nbsp;(.*?)</span>.*?</a>.*?'  # 电影别名
                             # + u'<div.*?class="bd">.*?<p.*?class="">.*?'
                             + u'导演: (.*?)&nbsp;&nbsp;&nbsp;'  # 导演
                             + u'主演: (.*?)<br>'  # 主演
                             + u'(.*?)&nbsp;/&nbsp;'  # 年份
                             + u'(.*?)&nbsp;/&nbsp;'  # 原产国
                             + u'(.*?)</p>'  # 类型
                             + u'.*?<div.*?class="star">.*?property="v:average">(.*?)</span>'  # 平均评分
                             + u'.*?<span>(.*?)人评价</span>.*?<p.*?class="quote">.*?'  # 评论数
                             + u'<span.*?class="inq">(.*?)</span>.*?</li>', re.S)  # 简评
        while self.start <= 225:
            page = self.getPage()
            movies = re.findall(pattern, page)
            for movie in movies:
                self.movieList.append([movie[0], movie[1], movie[2].lstrip('&nbsp;/&nbsp;'),
                                       movie[3].lstrip('&nbsp;/&nbsp;'), movie[4],
                                       movie[5], movie[6].lstrip(), movie[7], movie[8].rstrip(),
                                       movie[9], movie[10], movie[11]])

    def writeTxt(self):
        fileTop250 = open(self.filePath, 'w')
        try:
            for movie in self.movieList:
                fileTop250.write('电影排名：' + movie[0] + '\r\n')
                fileTop250.write('电影名称：' + movie[1] + '\r\n')
                fileTop250.write('外文名称：' + movie[2] + '\r\n')
                fileTop250.write('电影别名：' + movie[3] + '\r\n')
                fileTop250.write('导演姓名：' + movie[4] + '\r\n')
                fileTop250.write('参与主演：' + movie[5] + '\r\n')
                fileTop250.write('上映年份：' + movie[6] + '\r\n')
                fileTop250.write('制作国家/地区：' + movie[7] + '\r\n')
                fileTop250.write('电影类别：' + movie[8] + '\r\n')
                fileTop250.write('电影评分：' + movie[9] + '\r\n')
                fileTop250.write('参评人数：' + movie[10] + '\r\n')
                fileTop250.write('简短影评：' + movie[11] + '\r\n\r\n')
            print('文件写入成功...')
        finally:
            fileTop250.close()

    def main(self):
        print('正在从豆瓣电影Top250抓取数据...')
        self.getMovie()
        self.writeTxt()
        print('抓取完毕...')


DouBanSpider = MovieTop250()
DouBanSpider.main()