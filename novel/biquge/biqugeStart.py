
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import config
from novelcontent import NovelContent
from novelinfo import NovelInfo
from search import BiqugeSearch

__author__ = 'zhengxiaoming'
__date__ = '2018/11/6'

class BiqugeStart(object):

    def __init__(self,novelname):
        self.novelname = novelname

        self.biquge_novel_path = config.NOVEL_PATH + "/" + novelname + "/" + "biquge/"
        if not os.path.exists(self.biquge_novel_path):
            os.mkdir(self.biquge_novel_path)
        pass

    def req(self):
        biqugesearch = BiqugeSearch(self.novelname)
        searchBean = biqugesearch.parse(biqugesearch.req())
        print(searchBean)
        if searchBean :
            infoBean = NovelInfo(searchBean['novelurl'])
            chapters = infoBean.parse(infoBean.req())

            for chapter in chapters:
                chaptername = chapter['chapterName']
                chapterurl = chapter['chapterUrl']
                contentBean = NovelContent(chapterurl)
                print(chaptername,chapterurl)

                content = contentBean.parse(contentBean.getnovelcontent())
                print(chaptername,"开始保存...")
                self.saveChapter(chaptername, content)
                print(chaptername, "保存完成...")

    def saveChapter(self,chaptername,content):
        path =  self.biquge_novel_path + chaptername
        if os.path.exists(path):
            pass
        else:
            with open(path,'w') as file:
                file.write(content)


if __name__ == '__main__':

    biqugeBean = BiqugeStart('轮回乐园')
    biqugeBean.req()
    pass