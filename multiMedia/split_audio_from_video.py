#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.split_audio_from_video
# @Calendar: 2025-04-27 22:20
# @Time: 22:20
# @Author: mammon, kiramario
import datetime
from moviepy import AudioFileClip

def run():
    # 视频文件路径
    video_file_path = "C:\\Users\\mammon\\Desktop\\video_audio\\a.mp4"
    # 输出音频文件路径
    audio_output_path = "C:\\Users\\mammon\\Desktop\\video_audio\\a.wav"

    # 创建一个音频文件剪辑对象
    audio_clip = AudioFileClip(video_file_path)
    # 将音频写入到文件
    audio_clip.write_audiofile(audio_output_path)


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
