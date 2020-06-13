# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/11 5:54
# @FileName : quick_sort.py
# @SoftWare : PyCharm


def quick(items):
    """
    找分裂点（过程中即已经实现排序），分别对分裂点左右两半部分调用自身
    :param items:
    :return:
    """
    left = 0
    right = len(items) - 1
    quick_helper(items, left, right)
    return items


def quick_helper(items, left, right):
    if left < right:
        split_point = partition(items, left, right)
        # print(split_point, items)
        quick_helper(items, left, split_point - 1)
        quick_helper(items, split_point + 1, right)


def partition(items, left, right):
    pivot_value = items[left]
    left_cursor = left + 1
    right_cursor = right

    done = False
    while not done:
        # 左指针向右移动，遇到大于初始基准值时停止，此时左指针指向的是大于基准值的位置
        while left_cursor <= right_cursor and items[left_cursor] <= pivot_value:
            left_cursor += 1
        # 右指针向左移动，遇到小于初始基准值时停止，此时右指针指向的是小于基准值的位置
        while right_cursor >= left_cursor and items[right_cursor] >= pivot_value:
            right_cursor -= 1

        # 当右指针移到了左指针的左边，说明已经找了分裂点，即右指针指向的点, 交换右指针和基准值的位置
        if right_cursor < left_cursor:
            # 对初始基准值排序：初始基准值与右指针指向的点交换位置（即初始基准值找到了正确的顺序位置）
            items[left], items[right_cursor] = items[right_cursor], items[left]
            done = True
        # 左右指针停止后，两个指针指向的数据交换位置，即排序
        else:
            items[left_cursor], items[right_cursor] = items[right_cursor], items[left_cursor]

    return right_cursor


if __name__ == '__main__':
    items = [87, 6, 65, 12, 33, 2, 98, 3, 43, 23, 51]
    print(quick(items))
