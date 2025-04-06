#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.threading_1
# @Calendar: 2025-04-06 12:43
# @Time: 12:43
# @Author: mammon, kiramario
import datetime
import threading
import time


def worker(num):
    """子线程执行的函数"""
    print(f'Worker {num}-{threading.get_ident()} started.')
    time.sleep(3)
    print(f'Worker {num}-{threading.get_ident()} finish.')

def run():
    jobs = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        jobs.append(t)
        t.start()

    for i in range(5):
        jobs[i].join()

    print("all jobs finish, main thread exit")


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
