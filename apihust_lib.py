#!/usr/bin/python3
# coding=utf-8
import urllib
import urllib.request
import re
import os
class hustlib:
    def __init__(self,key):
        self.key=key
    def search(self):
        url="http://ftp.lib.hust.edu.cn/search*chx/X?SEARCH="+urllib.parse.quote(self.key)
        data=urllib.request.urlopen(url).read().decode('utf-8')
        about=[]
        about=re.compile(r'<span class="briefcitTitle">\n<a href=.*?">(.*?) / (.*?)</a>\n</span>\n<br />\n<span class="briefcitDetail">\n(.*?)\n<br />\n<span class="briefcitDetail">\n(.*?)<br />\n<br />\n<span class="briefcitDetail">\n(.*?)<br />',re.S).findall(data)
        if about!=[]:
            print(about)
        else:
            print('未找到')
        ndata=urllib.request.urlopen(url).read().decode('utf-8')
        while re.search('后一页',ndata):
            nurl=re.compile(r'<a href="(.*?)">后一页</a>').findall(ndata)
            url='http://ftp.lib.hust.edu.cn/'+nurl[0]
            z=input('\n有后一页，按y/Y进入后一页，按n/N退出\n请输入==>')
            if z=='y' or z=='Y':
                data=urllib.request.urlopen(url).read().decode('utf-8')
                about=[]
                about=re.compile(r'<span class="briefcitTitle">\n<a href=.*?">(.*?) / (.*?)</a>\n</span>\n<br />\n<span class="briefcitDetail">\n(.*?         )\n<br />\n<span class="briefcitDetail">\n(.*?)<br />\n<br />\n<span class="briefcitDetail">\n(.*?)<br />',re.S).findall(data)
                print(about)
            else:
                os.exit()
        print('当前页为最后一页\n')
keywords=input("请输入关键词==>")
x=hustlib(keywords)
x.search()
