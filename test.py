# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/13 8:46
# @FileName : test.py
# @SoftWare : PyCharm

import numpy as np
import random

from abstract.sorts.sort_integrate import SortIntegrate
from abstract.sorts import quick_sort

obj = SortIntegrate()

seqs = np.arange(31, 100, 3)
random.shuffle(seqs)
print('original: ', seqs)
bubble = obj.bubble(seqs)
print("bubble: ", bubble)
print()

seqs = np.arange(41, 110, 3)
random.shuffle(seqs)
print('original: ', seqs)
select = obj.select(seqs)
print('select：', select)
print()

seqs = np.arange(51, 120, 3)
random.shuffle(seqs)
print('original: ', seqs)
insert = obj.insert(seqs)
print('insert：', insert)
print()

seqs = np.arange(21, 90, 3)
random.shuffle(seqs)
print('original: ', seqs)
sheller = obj.sheller(seqs)
print('sheller：', sheller)
print()

seqs = np.arange(21, 79, 2)
seqs = [12, 43, 6, 23, 98, 33, 65, 2, 3, 87, 51]
random.shuffle(seqs)
print('original: ', seqs, len(seqs))
quicker = quick_sort.quick(seqs)
print('quick：', quicker)
print()
