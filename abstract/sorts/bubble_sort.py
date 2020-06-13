# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/13 8:19
# @FileName : bubble_sort.py
# @SoftWare : PyCharm


"""
反向遍历，两两比较，比较的同时伴随则数据交换
"""

import numpy as np
import random


def bubble(seq):
    length = len(seq)
    if length < 2:
        return seq

    exchange = False
    for cur_len in range(length - 1, 1, -1):
        for i in range(cur_len):
            if seq[i + 1] < seq[i]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                exchange = True
        if not exchange:
            break
    return seq
