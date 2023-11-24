#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu
"""

import os
from typing import *
import warnings


__all__ = ["InvalidPathWarning", "walk"]


class InvalidPathWarning(Warning):
    pass


def walk_path(path: Union[str, bytes], filter: Optional[Callable[[Union[str, bytes]], bool]] = None):
    if os.path.isdir(path):
        for (dirpath, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                filejoinname = os.path.join(dirpath, filename)
                if os.path.isfile(filejoinname) and (True if filter is None else filter(filejoinname)):
                    yield filejoinname
    elif os.path.isfile(path):
        if (True if filter is None else filter(path)):
            yield path
    else:
        warnings.warn(f"'{path}' is not a valid file or directory.", InvalidPathWarning)
    return


@overload
def walk(paths: str, filter: Optional[Callable[[str], bool]] = None) -> Generator[str, None, None]:
    ...

@overload
def walk(paths: bytes, filter: Optional[Callable[[bytes], bool]] = None) -> Generator[bytes, None, None]:
    ...

@overload
def walk(paths: List[str], filter: Optional[Callable[[str], bool]] = None) -> Generator[str, None, None]:
    ...

@overload
def walk(paths: List[bytes], filter: Optional[Callable[[bytes], bool]] = None) -> Generator[bytes, None, None]:
    ...

def walk(paths: Union[List[str], List[bytes], str, bytes], filter: Optional[Callable[[Union[str, bytes]], bool]] = None):
    if isinstance(paths, (list, tuple)):
        for path in paths:
            for filepath in walk_path(path, filter):
                yield filepath
    else:
        for filepath in walk_path(paths, filter):
            yield filepath
    return


if __name__ == '__main__':
    for filepath in walk(b".", lambda x: os.path.splitext(x)[1].lower() == b'.py'):
        print(repr(filepath))
