#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import config

from biqugeStart import BiqugeStart

__author__ = 'zhengxiaoming'
__date__ = '2018/11/6'


if __name__ == '__main__':
    if not os.path.exists(config.NOVEL_PATH):
        os.mkdir(config.NOVEL_PATH)

    novelname = input('please enter your novel: ')

    if not os.path.exists(config.NOVEL_PATH + "/" + novelname):
        os.mkdir(config.NOVEL_PATH + "/" + novelname)

    biqugeBean = BiqugeStart(novelname)
    biqugeBean.req()
    pass