#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.6

import os
import jieba.posseg as posseg
import jieba.analyse

from ALM_app.etc import filePathConf

__author__ = 'Swollow <cs_zhlou@163.com>'
__time__ = '2019/6/16 0016 16:47'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
jieba.load_userdict(filePathConf.absPathDict[filePathConf.DICT])

'''
Chinese Word Segmentation: 中文分词
'''

'''
e.g.
    Input: str
        "左前臂"
    Output: list[pair(str, str)]
        [pair('左', 'm'), pair('前臂', 'n')]
or
    Input: [str]
        ["左前臂", "右前臂"]
    Output: [list[pair(str, str)]]
        [[pair('左', 'm'), pair('前臂', 'n')], [pair('右', 'm'), pair('前臂', 'n')]]
'''


def cnWord_seg(cnText):
    cnString_seg = []
    textType = type(cnText)
    stopwords = getStopwords(filePathConf.absPathDict[filePathConf.STOP_WORDS])
    if textType == str:
        sentence = list(posseg.cut(cnText))
        sentence_segment = []
        for word, pos in sentence:
            if not word.strip():
                continue
            word_stripped = word.strip()  # word strip
            if word_stripped in ['°', '℃', '%']:  # revise
                sentence_segment.append(posseg.pair(word, 'm'))
            elif word_stripped not in stopwords:  # filter stopwords
                sentence_segment.append(posseg.pair(word_stripped, pos))
            else:
                pass
        cnString_seg = sentence_segment
    elif textType == list:
        for cnTextItem in cnText:
            cnString_seg.append(cnWord_seg(cnTextItem))
    else:
        pass
    return cnString_seg


def getStopwords(path_stopwords):
    with open(path_stopwords, "r", encoding='utf-8') as f:
        lines = f.readlines()
    f.close()
    stopwords = [line.strip() for line in lines]
    return stopwords


def main():
    list1 = [
        "左前,，？/、\’‘“”:：；;！@#￥%……&（）——!@#$%^&*()",
        [
            "左前",
            ",，？/、\’‘“”:：；;！@#￥%……&（）——!@#$%^&*()_左前"
        ]
    ]
    print(cnWord_seg(list1))
    temp_list = cnWord_seg(",，？/、\’‘“”:：；;！@#￥%……&（）——!@#$%^&*()_左前")
    print(temp_list)
    print(temp_list[0])
    print(type(temp_list[0]))

if __name__ == '__main__':
    main()
