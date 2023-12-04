#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    比较位图是否相等的实用工具
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
import os
import sys
from warnings import warn
import argparse

import image_compare
import dir_walker
from utils.argparse import ExtNameAction
from utils.type import TypicalPathType


def parsearg(argv: List[str]):
    parser = argparse.ArgumentParser(
        description="图片比较程序 [Xs Python Utilities  Copyright (C) 2023  Xiao Siyu]",
        epilog="例如：{prog} -m RGBA -l .png .bmp --all ./patha ./pathb".format(prog=os.path.basename(argv[0]))
    )
    parser.add_argument("input_files", type=str, help="输入文件或文件夹的路径")
    parser.add_argument("refer_files", type=str, help="参考文件或文件夹的路径")
    parser.add_argument("-m", "--mode", default=None, type=str, help=f"比较模式（PIL编码），默认为自动。允许模式：{image_compare.PIL_MODES}")
    parser.add_argument("-l", "--filter", action=ExtNameAction, nargs='+', help="扩展名过滤白名单 (\".*\")。用于限制需要处理的文件。", metavar=".EXT")
    # parser.add_argument("-M", "-multi-threading", action='store_true', help="开启多线程模式 [=%(default)s]")  # TODO
    msgexgrp = parser.add_mutually_exclusive_group(required=False)
    msgexgrp.add_argument("-a", "--all", action='store_const', const="all", default="all", help="输出所有的比较结果", dest="message")
    msgexgrp.add_argument("-s", "--same", action='store_const', const="same", help="输出相同的比较结果", dest="message")
    msgexgrp.add_argument("-d", "--diff", action='store_const', const="diff", help="输出不同的比较结果", dest="message")
    args = parser.parse_args(argv[1:])
    # print(args)
    return args


def compare_one_img(cmp_path: TypicalPathType, ref_path: TypicalPathType, *,
                    mode: Optional[str] = None,
                    message: Literal["all", "same", "diff", ] = "all"):
    if not os.path.exists(cmp_path):
        print(f"'{cmp_path}' 不存在")
        return False
    if not os.path.exists(ref_path):
        print(f"'{ref_path}' 不存在")
        return False
    same = image_compare.image_compare(cmp_path, ref_path, mode=mode)
    if same:
        if message in ("all", "same"):
            print(f"'{cmp_path}' 与 '{ref_path}' 相同")
    else:
        if message in ("all", "diff"):
            print(f"'{cmp_path}' 与 '{ref_path}' 不同")
    return same


def compare_folder(cmp_folder_path: TypicalPathType, ref_folder_path: TypicalPathType,
                   filter_list: Optional[List[str]] = None,
                   *,
                   mode: Optional[str] = None,
                   message: Literal["all", "same", "diff", ] = "all"):
    for cmp_path in dir_walker.walk(cmp_folder_path, None if filter_list is None else (lambda x: os.path.splitext(x)[1].lower() in filter_list)):
        rel_path = os.path.relpath(cmp_path, cmp_folder_path)
        ref_path = os.path.join(ref_folder_path, rel_path)
        # print(rel_path, '\t', cmp_path, '\t', ref_path)
        compare_one_img(cmp_path, ref_path, mode=mode, message=message)
    return


def main(argv: List[str]):
    args = parsearg(argv)
    input_files = args.input_files
    refer_files = args.refer_files

    if (os.path.isfile(input_files) and os.path.isfile(refer_files)):
        if args.filter is not None:
            print("比较两个文件时过滤器无效")
        compare_one_img(input_files, refer_files, mode=args.mode, message=args.message)
    elif (os.path.isdir(input_files) and os.path.isdir(refer_files)):
        compare_folder(input_files, refer_files, args.filter, mode=args.mode, message=args.message)
    else:
        raise ValueError(f"type of '{input_files}' and '{refer_files}' is different")
    return


if __name__ == '__main__':
    # print("sys.argv =", sys.argv)
    main(sys.argv)
