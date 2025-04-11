#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.time_utils
# @Calendar: 2025-04-09 23:40
# @Time: 23:40
# @Author: mammon, kiramario
import datetime


"""
字符串时分秒转换成秒 h:m:s
"""
def hms_str_to_sec(x):
    h, m, s = x.strip().split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)