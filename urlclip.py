#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    将URL快捷方式裁剪到最简
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


import os
import sys
# import subprocess
from pprint import pprint
import configparser


def isurlfile(filename):
    return os.path.splitext(filename)[1].lower() == '.url'

def get_am_time_ns(filename):
    sr = os.stat(filename)
    return (sr.st_atime_ns, sr.st_mtime_ns)


def urlclip(urlfile, *, encoding='cp936'):
    print(urlfile)
    amtimens1 = get_am_time_ns(urlfile)
    cfg1 = configparser.ConfigParser(strict=False, interpolation=None)
    cfg1.read(urlfile, encoding=encoding)
    if cfg1.has_option("InternetShortcut", "url"):
        cfg2 = configparser.ConfigParser(strict=False, interpolation=None)
        cfg2.add_section("InternetShortcut")
        cfg2.set("InternetShortcut", "url", cfg1.get("InternetShortcut", "url"))
        cfg2.set("InternetShortcut", "url", cfg1.get("InternetShortcut", "url").split('#')[0])
        with open(urlfile, 'w', encoding=encoding) as f:
            cfg2.write(f, space_around_delimiters=False)
        urlrename(urlfile)
        os.utime(urlfile, ns=amtimens1)
    else:
        print(f"'{urlfile}' is not a valid url file.")
    return


def urlrename(urlfile):
    (root, ext) = os.path.splitext(urlfile)
    newname = root+ext.lower()
    os.rename(urlfile, newname)


if __name__ == "__main__":
    # pprint(sys.argv[1:])
    for path in sys.argv[1:]:
        # print()
        if os.path.isdir(path):
            for (dirpath, dirnames, filenames) in os.walk(path):
                for filename in filenames:
                    if isurlfile(filename):
                        urlclip(os.path.join(dirpath, filename))
        else:
            if isurlfile(path):
                urlclip(path)
            else:
                print(f"'{path}' is not a valid url file.")
    os.system('pause')
