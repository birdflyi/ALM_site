#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.6

import warnings

from ALM_app.etc import filePathConf
from sklearn.exceptions import DataConversionWarning

from ALM_app.script.utils.logUtils.setup_logging import setup_logging

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=DataConversionWarning, module='sklearn')

__author__ = 'Swollow <cs_zhlou@163.com>'
__time__ = '2019/6/16 0016 16:47'

# ----------------------------------------------------------------------------------------------------------------------
#  Setup logging
# ----------------------------------------------------------------------------------------------------------------------
setup_logging()

# ----------------------------------------------------------------------------------------------------------------------
#  Get file path configurations
# ----------------------------------------------------------------------------------------------------------------------
absPaths = filePathConf.absPathDict
