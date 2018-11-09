#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from html.parser import HTMLParser

import requests
import urllib3

__author__ = 'zhengxiaoming'
__date__ = '2018/11/6'


class BiqugeSearch(object):

    def __init__(self, novelName):
        self.url = 'http://zhannei.baidu.com/cse/search?p=0&s=5199337987683747968&area=1&q=' + novelName
        self.novelname = novelName
        print(self.url)

    def req(self):
        urllib3.disable_warnings()
        r = requests.get(self.url, verify=False)
        r.encoding = 'utf-8'
        return r.text

    def parse(self, html):
        myparsaer = SearchParser()
        myparsaer.feed(html)
        myparsaer.close()
        for novel in myparsaer.novels:
            if novel['novelname'] == self.novelname:
                return novel


    pass


class SearchParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.novels = []
        self.start = None
        self.process = None

    def handle_starttag(self, tag, attrs):
        if tag == 'h3':
            for (variable, value) in attrs:
                if variable == 'class' and value == 'result-item-title result-game-item-title':
                    self.start = 'result-item-title result-game-item-title'

        if self.start:
            if tag == 'a':
                if (len(attrs)) == 0:
                    pass
                else:
                    for (variable, value) in attrs:
                        if variable == 'href':
                            novel = {}
                            novel['novelurl'] = value
                            self.novels.append(novel)
                            self.process  = True
                        if self.process and variable == 'title':
                            novel = self.novels[-1]
                            novel['novelname'] = value

    def handle_endtag(self, tag):
        if tag == 'h3':
            if self.start:
                self.start = None


if __name__ == '__main__':
    myserarch = BiqugeSearch("轮回乐园");
    response = myserarch.req()
    novels = myserarch.parse(response)
    for novel in novels:
        if novel['novelname'] == '轮回乐园':
            print(novel)

    pass
