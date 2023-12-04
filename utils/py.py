#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    Python语言相关实用工具
"""


__all__ = [
    "getFullTypeName", "getClassFullName",
]


import builtins


def getClassFullName(cls: type) -> str:
    if not isinstance(cls, type):
        raise TypeError(f"type except, but {getClassFullName(type(cls))} got")
    return cls.__qualname__ if cls.__module__ == builtins.__name__ else cls.__module__ + "." + cls.__qualname__


def getFullTypeName(obj):
    return getClassFullName(type(obj))
