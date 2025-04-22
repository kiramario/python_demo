#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.pip_install.py
# @Calendar: 2025-04-08 22:49
# @Time: 22:49
# @Author: mammon, kiramario
import datetime
import subprocess
import pip, sys, shlex, re
from pathlib import Path
from typing import List
from io import StringIO, TextIOBase
import io
from pyparsing import Word, alphas, OneOrMore, nums, Optional, ZeroOrMore, Literal

class CustomWriter(TextIOBase):
    def __init__(self):
        self.content = ""
    def write(self, text):
        self.content += text

def run():
    package = 'moviepy'
    cmd1 = [sys.executable, "-c", "import sys; print(sys.version)"]
    cmd_install = [sys.executable, "-m", "pip", "install", package]
    p = subprocess.Popen(cmd_install,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    stdout, stderr = p.communicate()

    parse_install_info(stdout)

# 此方法后面新版本是不准用了
def install(package):
    buffer = StringIO()
    sys.stdout = buffer
    sys.stderr = sys.stdout

    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
    output = buffer.getvalue()

    parse_install_info(output)
    # 还原标准输出
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    print("recover stdout, get content from buffer")
    print(output)

# 此方法后面新版本是不准用了
def install2(package):
    # 创建一个自定义的输出写入器
    custom_writer = CustomWriter()
    # 保存原来的标准输出
    original_stdout = sys.stdout
    # 重定向标准输出到自定义的写入器
    sys.stdout = custom_writer
    # 在这里执行需要输出的代码
    print("Hello, World!")
    print("This is a test.")
    # 还原标准输出
    sys.stdout = original_stdout
    # 打印重定向后的结果
    parse_install_info(custom_writer.content)

# TODO: extract parser, lexer, make my past experience valuable
def parse_install_info(stdout_str: str):
    success_installes = stdout_str.split("Successfully installed")[1]

    # 语法
    """
    package_version ::= alphas+ '-' nums+ '.' nums+ '.' nums+
    """
    aToz = Word(alphas)
    words = OneOrMore(aToz)

    package_name_a = words + Optional(Literal("-")) + Optional(words)
    package_name_b = words + Optional(Literal("_")) + Optional(words)
    package_name = Optional(package_name_a) + Optional(package_name_b)

    version = OneOrMore(Word(nums+"."))

    package_with_version = OneOrMore(package_name + "-" + version)

    print(success_installes)
    stats = package_with_version.parseString(success_installes)
    print(list(stats))

    # pattern = re.compile(r'[a-z]+\-(\d|\.)+', re.I)  # re.I 表示忽略大小写
    # package_raw_info = success_installes.split("\n")
    # print(package_raw_info)
    #
    # package_info = filter(
    #     lambda x: len(x) > 0 and pattern.match(x),
    #     map(lambda x: x.strip(), package_raw_info)
    # )
    # print(list(package_info))
    # refresh_requirement(list(package_info))

def refresh_requirement(packages: List[str]):
    pip_install_py_path = Path(sys.argv[0])
    requirements_path = pip_install_py_path.parent / "requirements.txt"
    print(requirements_path.resolve())

    with open(requirements_path.resolve(), "a") as f:
        for package in packages:
            name_version = package.split("-")
            f.write(f"{name_version[0]}=={name_version[1]}\n")

stdout_str = """
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
    aiohappyeyeballs-2.6.1 aiohttp-3.11.16
    

\r\n'

"""


if __name__ == "__main__":

    start = datetime.datetime.now()
    # run()
    # install("aiohttp")
    # install2("aiohttp")
    parse_install_info(stdout_str)

    # print(sys.executable)
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")


