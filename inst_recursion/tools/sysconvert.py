# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/23 16:48
# @FileName : sysconvert.py
# @SoftWare : PyCharm

"""
进制转换通用工具： bin_oct_hex_convert
思路：
    进制基base: 整数除 + 取余数 ---> 进制转换
    余数 总是 小于 进制基base
"""


def bin_oct_hex_convert(target, base):
    """
    非负整数进制转换通用工具, 任何进制(16进制及以下)均可，不仅限于bin oct 和 hex之间的进制转换
    :param target: 带转换的数字
    :param base:   转换后的结果的进制
    :return:
    """
    if not isinstance(target, int):
        raise TypeError(
            "'int' object expected instead of {}".format(
                type(target)))
    base_collection = "0123456789ABCDEF"
    if target < base:
        return base_collection[target]
    return bin_oct_hex_convert(target // base, base) + \
        base_collection[target % base]


if __name__ == '__main__':
    num_input = 235
    base_input = 2
    oct_bin = bin_oct_hex_convert(num_input, base_input)
    print(oct_bin, type(oct_bin))
