#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zhengxiaoming'
__date__ = '2018/11/6'

'''
小说内容
'''
import urllib3
import requests
from html.parser import HTMLParser

class NovelContent(object):

    def __init__(self,chapterurl):
        self.chapterurl = chapterurl

    def getnovelcontent(self):
        urllib3.disable_warnings()
        r = requests.get(self.chapterurl, verify=False)
        r.encoding = 'utf-8'
        return r.text

    def parse(self, html):
        myparsaer = ContentParser(self.chapterurl)
        myparsaer.feed(html)
        myparsaer.close()
        return myparsaer.content

    pass


class ContentParser(HTMLParser):

    def __init__(self, chapterurl):
        HTMLParser.__init__(self)
        self.content = ''
        self.start = None
        self.processing = None
        self.chapterurl = chapterurl

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for (variable, value) in attrs:
                if variable == 'id' and value == 'content':
                    self.start = 'content'

    def handle_endtag(self, tag):
        if tag == 'div':
            if self.start:
                self.start = None

    def handle_data(self, data):
        if self.start:
            self.content = self.content + "\n"
            self.content = self.content + data


if __name__ == '__main__':
    url = 'https://www.xbiquge6.com//77_77513/1228516.html'
    n = NovelContent(url)
    text = n.getnovelcontent()
    content = n.parse(text)
    print(content)
