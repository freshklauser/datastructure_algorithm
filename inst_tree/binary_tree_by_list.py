# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/17 15:07
# @FileName : binary_tree_by_list.py
# @SoftWare : PyCharm

"""
树的嵌套列表表达式： list实现
递归的嵌套列表实现二叉树，由具有3个元素的列表实现：[root, left, right]
    第1个元素是根节点的值（是一个数据项）
    第2个元素是左子树（是一个列表）
    第3个元素是右子树（是一个列表）

嵌套列表法的优点：
    子树的结构与树相同，是一种递归数据结构
    易扩展到多叉树，仅需要增加列表元素即可
"""


def binary_tree(root):
    return [root, [], []]


def insert_left(root, new_branch):
    """
    将新节点插入树中作为其直接的左子节点（如果已有左子节点，则把原左子节点作为
    新插入节点的左子节点，新插入节点做直接的左子节点）
    :param root:
    :param new_branch:  新插入的树作为当前节点的左子树
    :return:            新的树
    """
    tmp = root.pop(1)
    if len(tmp) > 1:
        # tmp时binary_tree的三元素列表[root,left,right]，当tmp为叶子节点时为[]
        root.insert(1, [new_branch, tmp, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    """
    将新节点插入树中作为其直接的右子节点（如果已有右子节点，则把原右子节点作为
    新插入节点的右子节点，新插入节点做直接的右子节点）
    :param root:
    :param new_branch:  新插入的树作为当前节点的右子树
    :return:            新的树
    """
    tmp = root.pop(2)
    if len(tmp) > 1:
        # tmp时binary_tree的三元素列表[root,left,right]，当tmp为叶子节点时为[]
        root.insert(2, [new_branch, [], tmp])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


if __name__ == '__main__':
    r = binary_tree(3)
    insert_left(r, 4)
    insert_left(r, 5)
    insert_right(r, 6)
    insert_right(r, 7)
    left_branch = get_left_child(r)
    print(left_branch)
    set_root_val(left_branch, 9)
    print(r)
    insert_right(left_branch, 11)
    print(r)
    print(get_right_child(get_right_child(r)))

