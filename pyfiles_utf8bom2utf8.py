#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    批量将Python源文件的编码从UTF-8-bom修改为UTF-8
"""

__author__ = "Xiao Siyu"
__copyright__ = """\
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
