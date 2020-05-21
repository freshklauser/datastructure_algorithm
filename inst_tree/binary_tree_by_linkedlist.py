# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/17 15:39
# @FileName : binary_tree_by_linkedlist.py
# @SoftWare : PyCharm

"""
利用链表构建二叉树类
类功能函数：
    insert_left_child
    insert_right_child
    get_left_child
    get_right_child
    set_root_val
    get_root_val
"""


class BinaryTree:
    def __init__(self, root_obj):
        self.data = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, new_node_val):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node_val)
        else:
            new_node = BinaryTree(new_node_val)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right_child(self, new_node_val):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node_val)
        else:
            new_node = BinaryTree(new_node_val)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, obj_val):
        self.data = obj_val

    def get_root_val(self):
        return self.data


if __name__ == '__main__':
    r = BinaryTree('a')
    r.insert_left_child('b')
    r.insert_right_child('c')
    r.get_right_child().set_root_val('hello')
    r.get_left_child().insert_right_child('dd')
    print(r.left_child.right_child.data)
