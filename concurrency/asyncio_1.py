#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.asyncio
# @Calendar: 2025-04-15 00:16
# @Time: 0:16
# @Author: mammon, kiramario
import datetime

"""
https://zhuanlan.zhihu.com/p/688073007
"""
def run():
    pass


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
