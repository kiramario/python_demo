import datetime
import subprocess
import pip, sys
from pathlib import Path
from typing import List
from io import StringIO, TextIOBase
from pyparsing import Word, nums,  Literal, Combine

class CustomWriter(TextIOBase):
    def __init__(self):
        self.content = ""
    def write(self, text):
        self.content += text

def write_requirement(installed: str):
    requirement_path = Path.cwd() / "requirements.txt"

    if not requirement_path.exists():
        with open(str(requirement_path), 'w') as f:
            pass

    with open(str(requirement_path), "a+") as f:
        f.write("\n")
        f.write(installed)

def run(package_name: str):
    cmd1 = [sys.executable, "-c", "import sys; print(sys.version)"]
    cmd_install = [sys.executable, "-m", "pip", "install", package_name]
    p = subprocess.Popen(cmd_install,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    stdout, stderr = p.communicate()

    if isinstance(stdout, bytes):
        stdout = stdout.decode('utf-8')

    installed = parse_install_info(stdout, package_name)

    if not installed:
        print("nothing write")
        return

    package_name_end_index = installed.index(package_name) + len(package_name)
    to_write = installed[0 : package_name_end_index] + "==" + installed[ package_name_end_index + 1:]
    write_requirement(to_write)

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
def parse_install_info(stdout_str: str, package_name: str):
    dash = Literal("-")
    version = Combine(Word(nums) + ("." + Word(nums)) * 2)
    package_expr = Combine(Literal(package_name) + dash + version)
    res = package_expr.searchString(stdout_str)
    if len(res) == 0:
        return ""
    return res[0][0]

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

stdout_str_2 = """
b'Requirement already satisfied: jinja2 in c:\\alluserapplication\\anaconda3\\envs\\demo\\lib\\site-packages (3.1.6)\r\nRequirement already satisfied: MarkupSafe>=2.0 in c:\\alluserapplication\\anaconda3\\envs\\demo\\lib\\site-packages (from jinja2) (3.0.2)\r\n'
"""


if __name__ == "__main__":
    package_name = "lxml" if len(sys.argv) == 1 else sys.argv[1]

    start = datetime.datetime.now()
    run(package_name)
    # install("aiohttp")
    # install2("aiohttp")
    # parse_install_info(stdout_str_2, package_name)
    # print(sys.executable)
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")


