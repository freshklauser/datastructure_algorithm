# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/23 15:45
# @FileName : Joseph_queue.py
# @SoftWare : PyCharm

"""
约瑟夫问题，即击鼓传花问题
N个人围成一个圈，从拿花的人开始，每次传到第k个人停止击鼓，拿花的人出列，最后剩谁
思路：
    双端队列模拟：队首的人(拿花的人)出队，随即再到队尾入队，算是一次花的传递
    传递了k次后，对首的人移除，不再入队，如此反复直到剩余一个人
队列：队尾入，队首出
"""

from collections import deque


def joseph_problem(name_list, out_num):
    # name_list 转化为 双端队列
    name_deque = deque()
    for item in name_list:
        name_deque.append(item)

    while len(name_deque) > 1:
        # 传递 out_num 次
        for i in range(out_num):
            name_deque.appendleft(name_deque.pop())
        # out_num 次传递完后，队首的人移除，不再入队
        name_deque.pop()

    return name_deque.pop()


if __name__ == '__main__':
    names = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'kk', 'mm', 'nn']
    num = 7
    res = joseph_problem(names, num)
    print(res)
