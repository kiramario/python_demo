#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python_demo.auth_demo1
# @Calendar: 2025-04-13 02:15
# @Time: 2:15
# @Author: mammon, kiramario
import datetime
import firebase_admin
from firebase_admin import auth, credentials
from firebase_admin.auth import ActionCodeSettings


def retrive_user_info():
    uid = "gzGd3TR6LlTFZzWxtJZe7rkvsDk2"
    user = auth.get_user(uid)
    user = auth.get_user_by_email(email)
    user = auth.get_user_by_phone_number(phone)

    print('Successfully fetched user data: {0}'.format(user.uid))

    result = auth.get_users([
        auth.UidIdentifier('uid1'),
        auth.EmailIdentifier('user2@example.com'),
        auth.PhoneIdentifier(+15555550003),
        auth.ProviderIdentifier('google.com', 'google_uid4')
    ])

    print('Successfully fetched user data:')
    for user in result.users:
        print(user.uid)

    print('Unable to find users corresponding to these identifiers:')
    for uid in result.not_found:
        print(uid)

    user = auth.create_user(
        email='user@example.com',
        email_verified=False,
        phone_number='+15555550100',
        password='secretPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=False)
    print('Sucessfully created new user: {0}'.format(user.uid))

    user = auth.create_user(
        uid='some-uid', email='user@example.com', phone_number='+15555550100')
    print('Sucessfully created new user: {0}'.format(user.uid))

    user = auth.update_user(
        uid,
        email='user@example.com',
        phone_number='+15555550100',
        email_verified=True,
        password='newPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=True)
    print('Sucessfully updated user: {0}'.format(user.uid))

    auth.delete_user(uid)
    print('Successfully deleted user')

    result = auth.delete_users(["uid1", "uid2", "uid3"])

    print('Successfully deleted {0} users'.format(result.success_count))
    print('Failed to delete {0} users'.format(result.failure_count))
    for err in result.errors:
        print('error #{0}, reason: {1}'.format(result.index, result.reason))

    # Start listing users from the beginning, 1000 at a time.
    page = auth.list_users()
    while page:
        for user in page.users:
            print('User: ' + user.uid)
        # Get next batch of users.
        page = page.get_next_page()

    # Iterate through all users. This will still retrieve users in batches,
    # buffering no more than 1000 users in memory at a time.
    for user in auth.list_users().iterate_all():
        print('User: ' + user.uid)


def email_generate():
    # Initialize app
    cred = credentials.Certificate("E:\\FTP_Server\\JOS@\\Projects\\pythonProjects\\python_demo\\secrets\\fir-fe63d-firebase-adminsdk-fbsvc-9f369cab31.json")
    default_app = firebase_admin.initialize_app(cred)

    # Generate password reset link
    email = "645364525@qq.com"
    # email = "zhangyangFBI@126.com" # 非注册email无法生成
    link = auth.generate_password_reset_link(email)

    # Now send 'link' via your email service
    print("Send this link to user:", link)
    action_code_settings = ActionCodeSettings(
        url="http://127.0.0.1:3001/firebase/auth?act=123",
        handle_code_in_app=True
    )
    link2 = auth.generate_sign_in_with_email_link(email, action_code_settings)
    print("Send this link to user:", link2)


def run():
    # cred = credentials.Certificate("E:\\FTP_Server\\JOS@\\Projects\\pythonProjects\\python_demo\\secrets\\fir-fe63d-firebase-adminsdk-fbsvc-9f369cab31.json")
    # default_app = firebase_admin.initialize_app(cred)


    # retrive_user_info("")
    email_generate()

if __name__ == "__main__":
    start = datetime.datetime.now()
    run()
    exec_time = (datetime.datetime.now() - start).total_seconds()
    print(f"run total spend: {exec_time:.3f}s\n")
