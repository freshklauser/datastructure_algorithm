# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/17 16:32
# @FileName : _stack.py
# @SoftWare : PyCharm


"""
抽象数据类型 Stack： python实现
    push(item): 添加元素到栈顶，无返回值
    pop():      删除栈顶元素并返回该元素，栈被修改
    peek():     查看栈顶元素，返回栈顶元素当不从栈中移除，栈不被修改(stack空时返回None)
    is_empty(): 返回栈是否为空 True or False
    size():     @property, 返回栈中有多少元素, Stack.size
"""


class Stack:
    def __init__(self):
        self.items = []
        self._count = 0

    @property
    def size(self):
        return self._count

    def is_empty(self):
        return self._count == 0

    def push(self, item):
        """栈顶添加元素"""
        self.items.append(item)
        self._count += 1

    def pop(self):
        """栈顶删除元素"""
        top_item = self.items.pop()
        self._count -= 1
        return top_item

    def peek(self):
        """返回栈顶元素 若栈为空，返回None"""
        return self.items[self._count - 1] if self._count != 0 else None


if __name__ == '__main__':
    ms = Stack()
    ms.push(1)
    ms.push(2)
    ms.push(13)
    item = ms.peek()
    ms.push(34)
    ms.pop()
    print(ms.items)
    print(item, ms.size)
