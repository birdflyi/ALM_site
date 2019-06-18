#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.6


__author__ = 'Swollow <cs_zhlou@163.com>'
__time__ = '2019/6/16 0016 16:47'

# ----------------------------------------------------------------------------------------------------------------------
#   Request Structure related stuff
# ----------------------------------------------------------------------------------------------------------------------
# current request protocol:
#     reqmethod='func1'
#     reqdata=[{"key":"value"}]
# reqmethod represent the process function called, marked as Request_CallProcessFunction, varied within range of
#   reqJson_SupportFunctions: ['func1', 'func2'], make sure these function has been implemented.
# reqdata represent the data submitted, marked as Request_SubmitData.

# Define the keys in map of request Json: reqJson_MapKeys
Request_CallProcessFunction = 0
Request_SubmitData = 1
# Define the functions which are valid in request Json only when supported by the server: reqJson_SupportFunctions
func1 = 0
func2 = 1

# Modify the value of dict: reqJson_MapKeys and reqJson_SupportFunctions if you want to change your request protocol.
# Make sure the value of your Request_CallProcessFunction(field) within your request should always belong to
#   dict reqJson_SupportFunction!

reqJson_MapKeys = {
    Request_CallProcessFunction: 'reqmethod',
    Request_SubmitData: 'reqdata',
}
reqJson_SupportFunctions = {
    func1: 'func1',
    func2: 'func2',
}
