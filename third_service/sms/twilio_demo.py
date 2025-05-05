#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.twilio_demo
# @Calendar: 2025-04-28 12:57
# @Time: 12:57
# @Author: mammon, kiramario
import datetime, json
from twilio.rest import Client
from os.path import expanduser, expandvars

def get_secrets():
    with open(expanduser('~/chat-robot.env')) as f:
        secrets = json.load(f)
    return secrets["twilio"]
twilio_secrets = get_secrets()

def run():
    account_sid = twilio_secrets["account_sid"]
    auth_token = twilio_secrets["auth_token"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+15746013908",
        to='+8618381068606',
        body='You have an appointment with Owl, Inc. on Friday, November 3 at 4:00 PM. Reply C to confirm.',)
    print(message.sid)


if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
