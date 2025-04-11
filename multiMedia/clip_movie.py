#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mitmproxyEnv.clip_movie
# @Calendar: 2024-08-09 01:22
# @Time: 1:22
# @Author: mammon, kiramario
import os, sys
import time
import argparse
from pathlib import Path
from moviepy import *
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(os.path.abspath(script_path))
root_dir = os.path.abspath(os.path.join(script_dir, os.path.pardir))
sys.path.insert(0, root_dir)

from common_utils.time_utils import hms_str_to_sec

os.environ['IMAGEMAGICK_BINARY'] = r"D:\PortableProjects\PHP\php_8.1.21_lavalite\ImageMagick-7.1.1-13-portable-Q16-HDRI-x64\magick.exe"


def clip_moive(
    source: str,
    target: str,
    cliplist: str
):
    # 解析切分片段
    start_end_list = [y for x in cliplist.split(",") for y in x.split("-")]

    multiple_start_end = list(zip(start_end_list[0::2], start_end_list[1::2]))

    source_path = Path(source)

    if not "mp4" in source_path.suffix and not "mkv" in source_path.suffix:
        raise Exception("suffix not support")
        return

    name_without_suffix = source_path.name.strip(source_path.suffix)

    if not target:
        target = source_path.parent.resolve()

    save_dir = Path(target) / "clip_save"

    os.makedirs(save_dir.resolve(), exist_ok=True)

    # TODO: create save if save directory not exits
    # TODO: MAKE A GUI
    # TODO: increase its adaptabiliy on possible circumstance
    for index, se in enumerate(multiple_start_end):
        index_str = f"0{index}" if index < 10 else f"{index}"
        movie_save_file = save_dir / f"{name_without_suffix}_{index_str}.{source_path.suffix}"

        clip = VideoFileClip(source_path.resolve())
        subc = clip.subclipped(se[0], se[1])
        video = CompositeVideoClip([subc]) #TODO: why array provided ?
        video.write_videofile(movie_save_file, fps=24, codec="libx264")

if __name__ == "__main__":
    # 创建解析器
    parser = argparse.ArgumentParser(description='clip movie')
    # 添加参数
    parser.add_argument('-s', '--source', help='to clip', required=True)
    parser.add_argument('-t', '--target', help='clip save')
    parser.add_argument('-c', '--cliplist', help='0:18:14-0:19:22, 0:20:22-0:22:59', required=True)

    # 解析参数
    args = parser.parse_args()

    clip_moive(args.source, args.target, args.cliplist)
    # print(f"args.source = {args.source}\r\nargs.target = {args.target}\r\nargs.cliplist = {args.cliplist}\r\n")
    # time.sleep(10)