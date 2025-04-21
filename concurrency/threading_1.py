#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.threading_1
# @Calendar: 2025-04-06 12:43
# @Time: 12:43
# @Author: mammon, kiramario
import datetime
import threading, signal
import time
from threading import Event

"""
normal threading, use Ctrl+C signal to interrupt main threading
and then consequencely stop the daemon threading through Event
"""

event = Event()

def spy_threading():
    while True:
        if event.is_set():
            break
        print(f'current threading num: {threading.active_count()}')
        time.sleep(1)

def worker(event, num):
    """子线程执行的函数"""
    print(f'Worker {num}-{threading.get_ident()} started.')
    for i in range(3):
        if event.is_set():
            # 在此添加退出前要做的工作，如保存文件等
            break

        print(f'Worker {num}-{threading.get_ident()} doing job.')
        time.sleep(3)
    print(f'Worker {num}-{threading.get_ident()} finish.')

def handler(signum, frame):
    global event
    event.set()
    print("receive a signal %d"%(signum))

def run():
    global event
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    jobs = [threading.Thread(target=spy_threading, daemon=True)]
    for i in range(5):
        t = threading.Thread(target=worker, args=(event, i,))
        jobs.append(t)

    for t in jobs:
        t.start()

    while 1:
        alive = False
        for j in jobs:
            alive = alive or j.is_alive()
        if not alive:
            break
        time.sleep(1)

    # for i in range(5):
    #     jobs[i+1].join()

    print("all jobs finish, main thread exit")


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
