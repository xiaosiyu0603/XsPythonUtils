#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    argpasre扩展
"""

__all__ = ["ExtNameAction", "CodingNameAction",]

from typing import *

import argparse
import codecs


class ExtNameAction(argparse.Action):
    """
        判断输入参数是否为扩展名
    """

    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: Sequence[str], option_string: str) -> None:
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
    """
        判断输入参数是否为有效编码
    """

    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: str, option_string: str) -> None:
        # print("values =", values)
        # print("option_string =", option_string)
        try:
            codecs.lookup(values)
        except LookupError as err:
            raise argparse.ArgumentError(self, str(err))
        setattr(namespace, self.dest, values)
        return
