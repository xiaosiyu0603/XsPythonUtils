#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu
"""

from argparse import ArgumentParser, Namespace
from typing import *
import sys
import os
import argparse
import codecs

from dir_walker import *


class ExtNameAction(argparse.Action):

    def __call__(self, parser: ArgumentParser, namespace: Namespace, values: Sequence[str], option_string: str) -> None:
        # print("values =", values)
        # print("option_string =", option_string)
        lower_values = list()
        for item in values:
            if not item.startswith("."):
                raise argparse.ArgumentError(self, f"'{item}' is not a valid filter (.*)")
            lower_values.append(item.lower())
        setattr(namespace, self.dest, lower_values)
        return


class CodingNameAction(argparse.Action):

    def __call__(self, parser: ArgumentParser, namespace: Namespace, values: str, option_string: str) -> None:
        # print("values =", values)
        # print("option_string =", option_string)
        try:
            codecs.lookup(values)
        except LookupError as err:
            raise argparse.ArgumentError(self, str(err))
        setattr(namespace, self.dest, values)
        return


def parsearg(argv: List[str]):
    parser = argparse.ArgumentParser(description="批量编码修改程序 [Xs Python Utilities  Copyright (C) 2023  Xiao Siyu]",
                                     epilog="数据无价，谨慎操作！")
    parser.add_argument("input_files", nargs='+', type=str, help="输入文件或文件夹的路径，并会被原位覆盖")
    parser.add_argument("-f", "--from", action=CodingNameAction, default="utf-8-sig", type=str, help="输入文件编码 [=\"%(default)s\"]", metavar="CODE", dest="fm")
    parser.add_argument("-t", "--to", action=CodingNameAction, default="utf-8", type=str, help="输出文件编码 [=\"%(default)s\"]", metavar="CODE", dest="to")
    parser.add_argument("-l", "--filter", action=ExtNameAction, nargs='+', help="扩展名过滤白名单 (\".*\") 出于安全原因强烈建议使用", metavar=".EXT")
    args = parser.parse_args(argv[1:])
    # print(args)
    return args


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


def main(argv: List[str]):
    args = parsearg(argv)
    # return
    path: List[str] = args.input_files
    fm: str = args.fm
    to: str = args.to
    filter_list: Optional[List[str]] = args.filter
    for filepath in walk(path, None if filter_list is None else (lambda x: os.path.splitext(x)[1].lower() in filter_list)):
        change_encoding(filepath, fm, to)
    os.system("pause")
    return


if __name__ == '__main__':
    # print("sys.argv =", sys.argv)
    main(sys.argv)
