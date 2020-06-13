# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/13 13:11
# @FileName : heaq_sort.py
# @SoftWare : PyCharm

"""
堆排序过程：
1、构将大根堆：将待排序数组构造成一个大根堆（元素上升） -- build_heap 非叶子节点逆序递归调用heapify
   确定最后一个非叶子节点（即last_node的parent_node）的index, 从这个点开始逆序遍历数组，对每个索引做heapify即可构造出大顶堆。
   其中，heapify函数中，对于每次最大值交换影响到的节点，需要递归调用heapifty实现受影响节点的堆化
2、固定一个最大值，由于大根堆的节点已经部分有序（父节点大于左右节点），秩序堆0节点做heapify即可
   遍历剩下节点的tree, 将根节点元素最大元素和最后一个元素交换位置，固定该最大值，将剩余的节点再构建大根堆
"""


def heaq_sort(tree):
    number = len(tree)
    build_heap(tree, number)
    for i in range(number - 1, 0, -1):
        # 交换堆顶最大值和最后一个节点，固定最大值
        tree[i], tree[0] = tree[0], tree[i]
        # 对当前堆(tree节点一直在减少，数量由i决定)的顶根节点做heapify即可
        heapify(tree, i, 0)
    return tree


def build_heap(tree, node_num):
    """
    对节点个数为 node_num 的数组构建大顶堆 (对节点调用heapify)
    思路：
        从最后一个非叶子节点开始，逆序遍历至根节点，堆每一个遍历的节点heapify
    :param tree:     当前待排序的数组
    :param node_num: 堆从根节点0处到索引 node_num - 1 处的 node_num 个节点
    :return:
    """
    last_node_index = node_num - 1
    parent_index = (last_node_index - 1) // 2
    for i in range(parent_index, -1, -1):
        heapify(tree, node_num, i)


def heapify(tree, node_num, index):
    """
    对数组中索引为index的节点做heapify
    在heapify过程中，由于最大值的数据交换影响到的节点需递归调用heapify
    原址交换，不需要额外辅助空间
    示例： [4, 7, 3] --> [7, 4, 3]
    :param tree:     带排序的数组
    :param node_num: 当前堆的节点数
    :param index:    heapify操作的节点
    :return:
    """
    if index >= node_num:
        return None
    left_node = 2 * index + 1
    right_node = 2 * index + 2
    max_index = index
    if left_node < node_num and tree[left_node] > tree[max_index]:
        max_index = left_node
    if right_node < node_num and tree[right_node] > tree[max_index]:
        max_index = right_node
    if max_index != index:
        # 最大值的点不是指定的index节点，需要交换数据将最大值交换到index
        tree[max_index], tree[index] = tree[index], tree[max_index]
        # 对交换后的max_index索引位的节点递归调用堆化
        heapify(items, node_num, max_index)


if __name__ == '__main__':
    items = [12, 43, 6, 23, 98, 33, 65, 2, 3, 87, 51]
    res = heaq_sort(items)
    print(res)
