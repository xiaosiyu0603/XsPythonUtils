#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    批量将Python源文件的编码从UTF-8-bom修改为UTF-8
"""

from typing import *
import sys
import os

from dir_walker import *


def change_encoding(filepath: str, fm="utf-8-sig", to="utf-8"):
    try:
        with open(filepath, 'r', encoding=fm) as fp:
            filebytes = fp.read()
        with open(filepath, 'w', encoding=to) as fp:
            fp.write(filebytes)
        print(f"File '{filepath}' converted.")
    except Exception as err:
        print(f"Error in '{filepath}': {repr(err)}")
    return


def main(path: List[str]):
    for filepath in walk(path, lambda x: os.path.splitext(x)[1].lower() == '.py'):
        change_encoding(filepath, "utf-8-sig", "utf-8")
    return


if __name__ == '__main__':
    # print("sys.argv =", sys.argv)
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    os.system("pause")
