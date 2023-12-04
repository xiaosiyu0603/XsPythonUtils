#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Xs Python Utilities
    Copyright (C) 2023  Xiao Siyu

    比较图片是否相同
"""

__all__ = ["PIL_MODES", "image_compare", ]

from typing import *
import os
from warnings import warn

import PIL.Image
import PIL.ImageChops

from utils.type import TypicalPathType, check_type


PIL_MODES: Final = PIL.Image.MODES


def check_pilmode(mode: str):
    if mode not in PIL_MODES:
        raise ValueError(f"'mode' (is {repr(mode)}) is not allowed. Legal input: {PIL_MODES}")
    return


def to_pilimg(_in: Union[TypicalPathType, PIL.Image.Image]) -> PIL.Image.Image:
    if isinstance(_in, PIL.Image.Image):
        img = _in
    else:
        img = PIL.Image.open(_in)
    return img


def pilimg_to_same_mode(image_cmp: PIL.Image.Image, image_ref: PIL.Image.Image, mode: Optional[str]):
    if mode is None:
        # NOTE: 当image_cmp<RGBA>，image_ref<P> -> <RGB>，可能比较会出错
        if (image_cmp.mode == 'P') and (image_ref.mode == 'P'):
            image_ref = image_ref.convert()
            image_cmp = image_cmp.convert(image_ref.mode)
        elif (image_ref.mode == 'P'):
            image_ref = image_ref.convert(image_cmp.mode)
        elif (image_cmp.mode != image_ref.mode):
            image_cmp = image_cmp.convert(image_ref.mode)
    else:
        if mode == 'P':
            raise ValueError("mode 'P' is not suitable")
        image_ref = image_ref.convert(mode)
        image_cmp = image_cmp.convert(mode)
    return (image_cmp, image_ref)


def pilimg_compare_arbitrary(image_cmp: PIL.Image.Image, image_ref: PIL.Image.Image):
    image_diff = PIL.ImageChops.difference(image_cmp, image_ref)
    return (image_diff.getbbox() is None)


def pilimg_compare(image_cmp: PIL.Image.Image, image_ref: PIL.Image.Image, *, mode: Optional[str] = None):
    check_type("image_cmp", image_cmp, PIL.Image.Image)
    check_type("image_ref", image_ref, PIL.Image.Image)
    if mode is not None:
        check_pilmode(mode)

    if image_cmp.size != image_ref.size:
        return False

    (image_cmp, image_ref) = pilimg_to_same_mode(image_cmp, image_ref, mode)
    return pilimg_compare_arbitrary(image_cmp, image_ref)


def image_compare(cmp: Union[TypicalPathType, PIL.Image.Image], ref: Union[TypicalPathType, PIL.Image.Image],
                  *, mode: Optional[str] = None) -> bool:
    image_cmp = to_pilimg(cmp)
    image_ref = to_pilimg(ref)
    return pilimg_compare(image_cmp, image_ref, mode=mode)
