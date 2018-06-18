#!/usr/bin/env python3
# -*-coding:utf-8 -*-


def login(environ):
    print(environ.get('PATH_INFO'))
    return b'Login'


def logout(environ):
    print(environ.get('PATH_INFO'))
    return b'Logout'


def register(environ):
    print(environ.get('PATH_INFO'))
    return b'Register'


def fav(environ):
    print(environ.get('PATH_INFO'))
    with open('templates/favicon.ico', 'rb') as f:
        ico = f.read()
    return ico

