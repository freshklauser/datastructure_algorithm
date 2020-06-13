# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/17 15:52
# @FileName : parse_tree.py
# @SoftWare : PyCharm


""" 创建 表达式解析树 ---> 目的时为了利用解析树求表达式的值
树的应用：解析树（语法树）
表达式表示为树结构：
    叶节点保存操作树，内部节点保存操作符
全括号表达式 ((43+2)*3-(23-12)): '('表达式开始，')'表达式结束
    表达式层次界定计算优先级
    树的结构从上往上，优先级由高到低
    树中每个子树都表示一个子表达式，将子树替换为子表达式值的节点，即可实现求值。
表达式解析：
    从全括号表达式构建表达式解析树，利用表达式解析树对表达式求值，从表达式解析树恢复原表达式的字符串形式
步骤：
    (1) 全括号表达式要分解为单词Token列表。
    (2) 创建表达式解析式：从左到右扫描全括号表达式的每个单词，依据规则建立解析树
        当前单词是左括号，则为当前节点添加一个新节点作为其左子节点，当前节点下降为这个新节点；
        如果当前单词是操作符±*/，将当前节点的值设为此符号，为当前节点添加一个新节点作为其右子节点,当前节点下降为这个新节点；
        如果当前单词是操作数，将当前节点的值设为此数，当前节点上升到父节点；
        如果当前节点是右括号，则当前节点上升到父节点。
    Tips:
        上升到父节点：用一个栈来记录跟踪父节点
            当前节点下降时，将下降前的节点push入栈
            当前节点需要上升到父节点时，上升到pop出栈的节点即可
refers:
https://www.bilibili.com/video/BV1h7411m7BK?p=73
https://blog.csdn.net/weixin_43712064/article/details/104407494
"""

import operator
from abstract.basic.stack import Stack
from abstract.trees.binary_tree import BinaryTree


def build_parse_tree(expression_input):
    """
    输入要求：
        （1）每两个操作数和中间的操作符构成的运算都必须用 () 括起来，
        （2）且元素将必须 空格 隔开 如"( 82 + 2 ) * 2"
    :param expression_input:
    :return:
    """
    if not isinstance(expression_input, str):
        raise TypeError('Type of input attribution is not correct: str type expected')
    expression = expression_input.split()
    print(expression)
    # trace_stack: 跟踪记录父节点
    trace_stack = Stack()
    # 创建一个空的二叉树
    parse_tree = BinaryTree('')
    # trace_stack记录父节点
    trace_stack.push(parse_tree)
    # 当前树节点指针
    cursor_tree = parse_tree

    # 遍历 expression, 构造解析树 parse_tree
    for i in expression:
        if i == '(':
            # 指针树创建一个左子树，并将指针树（父节点）入栈, 移动指针下降到左子树（入栈下降）
            cursor_tree.insert_left_child('')
            trace_stack.push(cursor_tree)
            cursor_tree = cursor_tree.get_left_child()
        elif i in ['+', '-', '*', '/']:
            # 操作符：节点赋值i，创建右子树，并将赋值后的指针树入栈，移动指针树到其右子树（入栈下降）
            cursor_tree.set_root_val(i)
            cursor_tree.insert_right_child('')
            trace_stack.push(cursor_tree)
            cursor_tree = cursor_tree.get_right_child()
        elif i not in ['+', '-', '*', '/', ')']:
            # 操作数：指针树赋值为操作数，并将栈顶元素弹出，移动指针树到其父节点--即弹出的栈顶元素（出栈上升）
            cursor_tree.set_root_val(int(i))
            parent = trace_stack.pop()
            cursor_tree = parent
        elif i == ')':
            # 右括号,表达树结束，出栈上升
            parent = trace_stack.pop()
            cursor_tree = parent
        else:
            raise ValueError
    return parse_tree


def evaluate(parse_binary_tree):
    """
    计算解析树表达式
    :param parse_binary_tree:
    :return:
    """
    operator_hash = {'+': operator.add,
                     '-': operator.sub,
                     '*': operator.mul,
                     '/': operator.truediv}
    # 缩小规模，转化为左子数和右子树的operator操作
    left_child = parse_binary_tree.get_left_child()
    right_child = parse_binary_tree.get_right_child()

    if left_child and right_child:
        # 操作符映射
        func = operator_hash[parse_binary_tree.get_root_val()]
        # 递归调用
        return func(evaluate(left_child), evaluate(right_child))
    else:
        # 基本条件结束，返回根节点的值即为最后求的值
        return parse_binary_tree.get_root_val()


if __name__ == '__main__':
    exp = "( ( ( 82 + 2 ) * 5 ) - ( ( 4 * 20 ) / 5 ) )"
    # ['(', '(', '82', '+', '2', ')', '*', '5', ')']
    ptree = build_parse_tree(exp)
    result = evaluate(ptree)
    print(result)
