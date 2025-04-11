#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.pip_install.py
# @Calendar: 2025-04-08 22:49
# @Time: 22:49
# @Author: mammon, kiramario
import datetime
import subprocess
import pip, sys, shlex

def run():
    package = 'moviepy'
    cmd1 = [sys.executable, "-c", "import sys; print(sys.version)"]
    cmd_install = [sys.executable, "-m", "pip", "install", package]
    p = subprocess.Popen(cmd_install,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    stdout, stderr = p.communicate()

    # TODO: 解析输出，提取到requirements.txt中
    print('stdout: ')
    print(stdout)

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

if __name__ == "__main__":
    start = datetime.datetime.now()
    # run()

    print(sys.executable)
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")


"""
stdout: 
b'Collecting moviepy\r\n Downloading moviepy-2.1.2-py3-none-any.whl.metadata (6.9 kB)\r\n
Collecting decorator<6.0,>=4.0.2 (from moviepy)\r\n  Downloading decorator-5.2.1-py3-none-any.whl.metadata (3.9 kB)\r\n
Collecting imageio<3.0,>=2.5 (from moviepy)\r\n  Downloading imageio-2.37.0-py3-none-any.whl.metadata (5.2 kB)\r\n
Collecting imageio_ffmpeg>=0.2.0 (from moviepy)\r\n  Downloading imageio_ffmpeg-0.6.0-py3-none-win_amd64.whl.metadata (1.5 kB)\r\n
Collecting numpy>=1.25.0 (from moviepy)\r\n  Downloading numpy-2.2.4-cp310-cp310-win_amd64.whl.metadata (60 kB)\r\n
Collecting proglog<=1.0.0 (from moviepy)\r\n  Downloading proglog-0.1.11-py3-none-any.whl.metadata (794 bytes)\r\n
Collecting python-dotenv>=0.10 (from moviepy)\r\n  Downloading python_dotenv-1.1.0-py3-none-any.whl.metadata (24 kB)\r\n
Collecting pillow<11.0,>=9.2.0 (from moviepy)\r\n  Downloading pillow-10.4.0-cp310-cp310-win_amd64.whl.metadata (9.3 kB)\r\n
Collecting tqdm (from proglog<=1.0.0->moviepy)\r\n  Using cached tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)\r\n
Collecting colorama (from tqdm->proglog<=1.0.0->moviepy)

\r\n  

Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)\r\n
    Downloading moviepy-2.1.2-py3-none-any.whl (126 kB)\r\nDownloading decorator-5.2.1-py3-none-any.whl (9.2 kB)\r\n
    Downloading imageio-2.37.0-py3-none-any.whl (315 kB)\r\nDownloading imageio_ffmpeg-0.6.0-py3-none-win_amd64.whl (31.2 MB)\r\n  
    ---------------------------------------- 31.2/31.2 MB 405.4 kB/s eta 0:00:00\r\n
    Downloading numpy-2.2.4-cp310-cp310-win_amd64.whl (12.9 MB)\r\n   ---------------------------------------- 12.9/12.9 MB 313.5 kB/s eta 0:00:00\r\n
    Downloading pillow-10.4.0-cp310-cp310-win_amd64.whl (2.6 MB)\r\n   ---------------------------------------- 2.6/2.6 MB 495.6 kB/s eta 0:00:00\r\n
    Downloading proglog-0.1.11-py3-none-any.whl (7.8 kB)\r\n
    Downloading python_dotenv-1.1.0-py3-none-any.whl (20 kB)\r\nUsing cached tqdm-4.67.1-py3-none-any.whl (78 kB)\r\n
    
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)\r\n
Installing collected packages: python-dotenv, pillow, numpy, imageio_ffmpeg, decorator, colorama, tqdm, imageio, proglog, moviepy\r\n
Successfully installed 
    colorama-0.4.6 
    decorator-5.2.1 
    imageio-2.37.0 
    imageio_ffmpeg-0.6.0 
    moviepy-2.1.2 
    numpy-2.2.4 
    pillow-10.4.0 
    proglog-0.1.11 
    python-dotenv-1.1.0 
    tqdm-4.67.1

\r\n'

"""