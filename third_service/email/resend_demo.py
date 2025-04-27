#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.resend
# @Calendar: 2025-04-26 16:24
# @Time: 16:24
# @Author: mammon, kiramario
import datetime
import resend
from dotenv import load_dotenv
import os

load_dotenv()

def run():
    resend.api_key = os.getenv("RESEND_API_KEY")
    params: resend.Emails.SendParams = {
        "from": "you@email.kiramario.cn",
        "to": "645364525@qq.com",
        "subject": "Hello World",
        "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
    }

    r = resend.Emails.send(params)
    print(r)


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
