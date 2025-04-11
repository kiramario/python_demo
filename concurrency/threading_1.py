#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.threading_1
# @Calendar: 2025-04-06 12:43
# @Time: 12:43
# @Author: mammon, kiramario
import datetime
import threading
import time



def spy_threading():
    while True:
        print(f'current threading num: {threading.active_count()}')
        time.sleep(1)

def worker(num):
    """子线程执行的函数"""
    print(f'Worker {num}-{threading.get_ident()} started.')
    time.sleep(3)
    print(f'Worker {num}-{threading.get_ident()} finish.')

def run():
    jobs = [threading.Thread(target=spy_threading, daemon=True)]
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        jobs.append(t)

    for t in jobs:
        t.start()

    for i in range(5):
        jobs[i+1].join()

    print("all jobs finish, main thread exit")


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
