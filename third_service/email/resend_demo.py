#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.resend
# @Calendar: 2025-04-26 16:24
# @Time: 16:24
# @Author: mammon, kiramario
import datetime
import resend
from dotenv import load_dotenv
import os, json
from os.path import expanduser, expandvars

load_dotenv()

def get_secrets():
    with open(expanduser('~/chat-robot.env')) as f:
        secrets = json.load(f)
    return secrets["resend"]

resend_secrets = get_secrets()

def run():

    resend.api_key = resend_secrets["API_KEY"]
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
