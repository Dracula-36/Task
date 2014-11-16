#!/usr/bin/python3
# coding=utf-8
import urllib
import urllib.request
import re
def get(url):
    data=urllib.request.urlopen(url).read().decode('utf-8')
    about=[]
    about=re.compile(r'<span class="briefcitTitle">\n<a href=.*?">(.*?) / (.*?)</a>\n</span>\n<br />\n<span class="briefcitDetail">\n(.*?)\n<br />\n<span class="briefcitDetail">\n(.*?)<br />\n<br />\n<span class="briefcitDetail">\n(.*?)<br />',re.S).findall(data)
    if about==[]:
        print('未找到')
    return (about)
def show(url):
    content=get(url)
    for i in range(0,len(content)):
        print('书名:《{0}》'.format(content[i][0]))
        print('作者:',content[i][1])
        print('主编:',content[i][2])
        print('出版相关信息:',content[i][3])
        print('简介:{0}\n'.format(content[i][4]))
def next(url):
    ndata=urllib.request.urlopen(url).read().decode('utf-8')
    if re.search('后一页',ndata):
        nurl=re.compile(r'<a href="(.*?)">后一页</a>').findall(ndata)
        url='http://ftp.lib.hust.edu.cn/'+nurl[0]
        z=input('有后一页，按y/Y进入后一页，按n/N退出\n请输入==>')
        if z=='y' or z=='Y':
            show(url)
            next(url)
    else:
        print('当前页为最后一页\n')
key=input("请输入关键词==>")
url="http://ftp.lib.hust.edu.cn/search*chx/X?SEARCH="+urllib.parse.quote(key)
show(url)
next(url)
