#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu
    生成随机密码，包括大小写字母、数字，可以指定密码长度
"""

import sys
import os

import secrets
import string
# python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters

__chars = string.ascii_letters + string.digits


def genPassword(length):
    """生成随机密码"""
    return ''.join(secrets.choice(__chars) for _ in range(length))  # 得出的结果中字符会有重复的
    # return ''.join(random.sample(__chars, 15))                    # 得出的结果中字符不会有重复的


def argv2(lenth=16, cycles=1, *args):
    try:
        lenth = int(lenth)
        cycles = int(cycles)
    except ValueError as err:
        print("非法参数：", f"{type(err).__name__}:", *(err.args))
        return

    for _ in range(cycles):
        print(genPassword(lenth))
    return


if __name__ == "__main__":
    argv2(*(sys.argv[1:]))
    os.system("pause")
