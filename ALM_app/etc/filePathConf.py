#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.6

import os

__author__ = 'Swollow <cs_zhlou@163.com>'
__time__ = '2019/6/16 0016 16:47'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Base directory: ALM_app

# ----------------------------------------------------------------------------------------------------------------------
#  Define file_names
# ----------------------------------------------------------------------------------------------------------------------
# Define the relative path of directory: data, algorithm_components
TERMS_WORD2VEC_TRAIN_MODEL = 0
DICT = 1
STOP_WORDS = 2

absPathDict = {
    TERMS_WORD2VEC_TRAIN_MODEL: os.path.join(
        BASE_DIR, 'algorithm_components/cacheModel/word2vec_train_model_baidubaike.pkl'),
    DICT: os.path.join(BASE_DIR, 'algorithm_components/dicts/local_dict.txt'),
    STOP_WORDS: os.path.join(BASE_DIR, 'algorithm_components/dicts/local_stopwords.txt'),
}

fileNameDict = {k: v.replace('\\', '/').split('/')[-1] for k, v in absPathDict.items()}

absDirDict = {k: '/'.join(v.replace('\\', '/').split('/')[:-1]) for k, v in absPathDict.items()}
