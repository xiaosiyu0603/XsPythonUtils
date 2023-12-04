#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    模拟C++同名定义的功能的实用工具

    参考：
    1. https://zh.cppreference.com/w/cpp/preprocessor/replace
    2. https://gcc.gnu.org/onlinedocs/cpp/Standard-Predefined-Macros.html
"""

import inspect

__all__ = [
    "PRETTY_FUNCTION", "__PRETTY_FUNCTION__",
    "LINE", "__LINE__", "FILE", "__FILE__",
]


def __PRETTY_FUNCTION__():
    """返回调用本函数的函数的名字和调用参数"""
    stack = inspect.stack()
    caller_frame = stack[1].frame
    caller_name = caller_frame.f_code.co_name
    caller_locals = caller_frame.f_locals
    caller_globals = caller_frame.f_globals
    # print("Calling function:", caller_name)
    # print("Local variables in calling function:", caller_locals)
    # print("Global variables in calling module:", caller_globals)
    kvstr = ", ".join((f"{key}={repr(value)}" for key, value in caller_locals.items()))
    return f"{caller_name}({kvstr})"


def __LINE__():
    """展开成源文件行号"""
    stack = inspect.stack()
    caller_frame = stack[1]
    line = caller_frame.lineno
    return line


def __FILE__():
    """展开成当前文件名，与`__file__`等价"""
    stack = inspect.stack()
    caller_frame = stack[1]
    filename = caller_frame.filename
    return filename


PRETTY_FUNCTION = __PRETTY_FUNCTION__
LINE = __LINE__
FILE = __FILE__
