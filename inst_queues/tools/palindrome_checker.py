# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/23 14:47
# @FileName : palindrome_checker.py
# @SoftWare : PyCharm


"""
给定一个字符串，判断是否是 回文词 plalindrome
思路：
    字符串元素添加到双端队列 deque
    每次从首尾分别取出一个元素，判断是否相等，
        不等则返回False,
        相等则继续从首尾取元素左比较 直至为空(偶数个元素)或元素剩1个(奇数个元素)
"""


from collections import deque


def pla_checker(str_input):
    """
    回文串检查器：判断输入的字符串是不是回文串
    :param str_input:
    :return: True or False
    """
    char_deque = deque()

    for item in str_input:
        char_deque.append(item)

    is_equal = True

    while len(char_deque) > 1 and is_equal:
        head = char_deque.popleft()
        tail = char_deque.pop()
        if head != tail:
            is_equal = False

    return is_equal


if __name__ == '__main__':
    s = 'abccba'
    res = pla_checker(s)
    print(res)
