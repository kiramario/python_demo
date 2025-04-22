#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.database
# @Calendar: 2025-04-21 11:28
# @Time: 11:28
# @Author: mammon, kiramario
import datetime
"""
db connection related stuff
"""

def run():
    pass


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
