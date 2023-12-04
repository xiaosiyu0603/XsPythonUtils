#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    类型相关实用工具
"""


__all__ = [
    "TypicalPathType",
    "check_type",
    "getClassFullName",
    "getFullTypeName",
]

from typing import *
import sys

from .py import *


# if sys.version_info >= (3, 12):
#     type TypicalPathType = Union[str, bytes]
# else:
if sys.version_info >= (3, 10):
    TypicalPathType: TypeAlias = Union[str, bytes]
else:
    TypicalPathType = Union[str, bytes]


def check_type(name, obj, cls, *, optional=False):
    if not ((optional and obj is None) or isinstance(obj, cls)):
        if isinstance(cls, tuple):
            cls_str = "(" + ", ".join(tuple(map(getClassFullName, cls))) + ")"
        else:
            cls_str = getClassFullName(cls)
        if optional:
            cls_str = cls_str + " or None"
        raise TypeError(f"'{name}' (is {obj!r}) must be {cls_str}, but {getFullTypeName(obj)} got.")
    return
