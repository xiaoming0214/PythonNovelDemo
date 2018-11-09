#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zhengxiaoming'
__date__ = '2018/11/6'

import urllib3
import requests
from html.parser import HTMLParser

'''
 小说详情包括章节
'''
class NovelInfo(object):

    def __init__(self,novelurl):
        self.host = 'https://www.xbiquge6.com/'
        self.novelurl = novelurl

    def req(self):
        urllib3.disable_warnings()
        r = requests.get(self.novelurl, verify=False)
        r.encoding = 'utf-8'
        return r.text

    def parse(self,html):
        myparsaer = InfoParser(self.host)
        myparsaer.feed(html)
        myparsaer.close()
        return myparsaer.chapters

    pass

class InfoParser(HTMLParser):

    def __init__(self,host):
        HTMLParser.__init__(self)
        self.chapters = []
        self.start = None
        self.processing = None
        self.host = host

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for (variable, value) in attrs:
                if variable == 'id' and value == 'list':
                    self.start = 'list'

        if self.start:
            if tag =='a':
                if(len(attrs)) == 0:
                    pass
                else:
                    for (variable,value) in attrs:
                        if variable == 'href':
                            self.processing = True
                            novel = {}
                            novel['chapterUrl'] = self.host + value
                            self.chapters.append(novel)

    def handle_endtag(self, tag):
        if tag == 'div':
            if self.start:
                self.start = None

    def handle_data(self, data):
        if self.processing:
            novel = self.chapters[-1]
            novel['chapterName'] = data
            self.processing = False

if __name__ == '__main__':

    url = 'https://www.xbiquge6.com/77_77513/'

    n = NovelInfo(url)
    text = n.req()
    chapters = n.parse(text)
    for chapter in chapters:
        print(chapter)
    pass