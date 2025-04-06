#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.__init__.py
# @Calendar: 2025-04-06 12:20
# @Time: 12:20
# @Author: mammon, kiramario
import datetime


def run():
    pass


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
