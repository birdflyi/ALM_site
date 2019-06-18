#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.6


"""
App package for project ALM_app. Based on django 2.0.7.

Copyright (C) 2019 Lou Zehua (Swollow <cs_zhlou@163.com>). All Rights Reserved.

To use, simply 'import ALM_app'!
"""
import pymysql

__author__ = 'Swollow <cs_zhlou@163.com>'
__time__ = '2019/6/16 0016 16:47'
# The following module attributes are no longer updated.
__version__ = '1.0.0'

# ----------------------------------------------------------------------------------------------------------------------
#   Miscellaneous module data
# ----------------------------------------------------------------------------------------------------------------------

#
# If you want to use MySQL database in django, use pymysql module as MySQLdb module
#
pymysql.install_as_MySQLdb()
