#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import re
import urllib
import os

_url = 'https://lysdefleur.gitbooks.io/objective-c-for-swift-developers/content/'
# docstring 根据 url 获取网页内容
#import    re


def gethtmlcontent(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def get_html_titles(html):
    reg = r'<li class="chapter " data-level=.*'
    title = re.compile(reg)
    titles = re.findall(title, html)
    return titles


htmlContent = gethtmlcontent(
    _url)
htmlTitles = get_html_titles(htmlContent)


def getDataLevel(html):
    reg = r'data-level=.{1,11}"'
    datalevel = re.compile(reg)
    datalevelInfo = re.search(datalevel, html)
    if datalevelInfo != None:
        return datalevelInfo.group(0)
    else:
        return None


def getDataPath(html):
    reg = r'data-path=".*"'
    path = re.compile(reg)
    pathinfo = re.search(path, html)
    if pathinfo != None:
        return pathinfo.group(0)
    else:
        return None

for title in htmlTitles:
    datalevel = getDataLevel(title)
    if datalevel != None:
        datalevelstrlen = len(datalevel)
        dirname = datalevel[12:datalevelstrlen-1]
        newdirname = dirname.replace('.', '_')  # 删除文件夹中 '.', 替换为 '-'
        curpath = os.getcwd() # 获取当前工作路径
        
        if os.path.exists(newdirname) == False:
            os.mkdir(newdirname) # 创建新文件夹
            # os.chmod(curpath+newdirname, stat.S_IRWXG) # 更改文件夹权限
    
    path = getDataPath(title)
    if path != None:
        pathstrlen = len(path)
        filename = path[11:pathstrlen-1]
        newfileName = filename.replace('/', '_')
        fileurl = _url + filename
        newhtmlcontent = gethtmlcontent(fileurl)
        
        # os.mknod(curpath+newdirname+newfileName)
        fo = open(curpath+'/'+newdirname+'/'+newfileName, "a")
        fo.write(newhtmlcontent)
    
