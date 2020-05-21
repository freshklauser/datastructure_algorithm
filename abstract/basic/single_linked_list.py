# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/17 16:56
# @FileName : single_linked_list.py
# @SoftWare : PyCharm


class Node(object):
    """定义节点类
    data: 节点保存的数据
    _next: 保存下一个节点对象
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)


class SingleLinkedList:
    def __init__(self):
        """初始化单链表属性
        head  : 单链表头节点
        length: 单链表长度
        """
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __repr__(self):
        """类的打印形式,遍历单链表打印
        Print items of single inked list as 1 --> 2 --> 3 --> ...
        执行语句 print(*instance) 时会自动调用该方法
        Returns:
            [str] -- [单链表的元素串起的字符串]
        """
        res = ''
        sign = ' --> '
        if self.is_empty():
            print("ATTENTION: empty single linked list")
        else:
            cursor = self.head
            while cursor:
                res += str(cursor.data) + sign
                cursor = cursor.next
        return res[:-len(sign)]

    def __getitem__(self, index):
        """获取指定索引对应的元素
        定义了__getitem__()方法，则实例对象（假设为P）就可以这样 P[key] 取值.
        该方法的 key 应该是整数值或 slice 对象，否则该方法会引发 KeyError 异常.
        该类中，index在这里不能时 slice 对象，只能是 Int
        Arguments:
            index {[int]} -- [getitem()定义的时针对某一个Index取值，因此这里index不能时slice]
        Returns:
            [type] -- [description]
        Raises:
            IndexError -- [description]
        """
        if self.is_empty() or index < 0 or index >= self.length:
            raise IndexError('Index out of range or object is empty.')
        else:
            return self.get_item(index)

    def __setitem__(self, index, data):
        if self.is_empty() or index < 0 or index >= self.length:
            raise IndexError('Index out of range or object is empty.')
        else:
            self.update(index, data)

    def _boundary_check(self, index):
        """索引边界检查
        Arguments:
            index {[int]} -- [索引]
        Returns:
            [bool] -- [True: 超过边界， False: 未超边界]
        """
        return index < 0 or index >= self.length

    def is_empty(self):
        return self.length == 0

    def clear(self):
        self.head = None
        self.length = 0

    def chain_table(self):
        """返回链表(head)"""
        return self.head

    def append(self, data_node):
        """尾部添加元素
        Arguments:
            data_node {[type(node.data) or Node]} -- [待添加的节点值或节点]
        """
        item = data_node if isinstance(data_node, Node) else Node(data_node)

        if not self.head:
            # head 为空时
            self.head = item
            self.length += 1
        else:
            # head 不为空时
            cursor = self.head
            while cursor.next:
                cursor = cursor.next
            # 指针移动到最后一个元素后，指向item, 同时长度+1
            cursor.next = item
            self.length += 1

    def delete(self, index):
        """删除指定index处的元素
        Arguments:
            index {[int]} -- [索引]
        Tips:
            非空检查和边界检查, first和last需要单独讨论
        """
        if self._boundary_check(index):
            raise IndexError('Index out of range')
        if self.is_empty():
            print("ATTENTION: empty single linked list")

        if index == 0:
            # 单独讨论删除头节点的情况
            self.head = self.head.next
            self.length -= 1
        else:
            cursor = self.head
            pre_node = self.head
            ind = 0
            while cursor.next and ind < index:
                ind += 1
                pre_node = cursor
                cursor = cursor.next
            if ind == index:
                pre_node.next = cursor.next
                ' ATTENTION: self.length needs to be updated altogether! '
                self.length -= 1

    def insert(self, index, data_node):
        """指定index处插入元素
        Arguments:
            index {[type]} -- [索引]
            data_node {[type]} -- [节点值或节点]
        Raises:
            IndexError -- [description]
        Tips:
            1) 头节点单独讨论
            2) 尾节点即尾部插入不能通过insert实现，需要通过append方法实现
        """
        if self._boundary_check(index):
            raise IndexError('Index out of range')
        if self.is_empty():
            print("ATTENTION: empty single linked list")

        item = data_node if isinstance(data_node, Node) else Node(data_node)

        if index == 0:
            # 单独讨论头节点位置的插入
            item.next = self.head
            self.head = item
            self.length += 1
        else:
            cursor = self.head
            pre_node = self.head
            ind = 0
            while cursor.next and ind < index:
                ind += 1
                pre_node = cursor
                cursor = cursor.next
            if ind == index:
                pre_node.next = item
                item.next = cursor
                ' ATTENTION: self.length needs to be updated altogether! '
                self.length += 1

    def update(self, index, data):
        """更新index处的节点值
        Arguments:
            index {[type]} -- [索引]
            data {[type]} -- [更新后的节点值]
        Raises:
            IndexError -- [description]
        Tips:
            1) 头节点的不需要单独考虑
        """
        if self._boundary_check(index):
            raise IndexError('Index out of range')
        if self.is_empty():
            print("ATTENTION: empty single linked list")

        cursor = self.head
        ind = 0
        while cursor.next and ind < index:
            ind += 1
            cursor = cursor.next
        if ind == index:
            cursor.data = data

    def get_item(self, index):
        """获取指定index处的节点值
        Arguments:
            index {[type]} -- [索引]
        Returns:
            [type] -- [节点值]
        Raises:
            IndexError -- [description]
        Tips:
            1) 头节点的不需要单独考虑
        """
        if self._boundary_check(index):
            raise IndexError('Index out of range')
        if self.is_empty():
            print("ATTENTION: empty single linked list")

        cursor = self.head
        ind = 0
        while cursor.next and ind < index:
            ind += 1
            cursor = cursor.next

        return cursor.data

    def get_all_index(self, data, all_instead_first=True):
        """获取data对应的所有索引
        Arguments:
            data {[type]} -- [description]
        Keyword Arguments:
            all_instead_first {bool} -- [获取所有索引还是第一条索引]
            (default: {True，获取所有索引})
        Returns:
            [list] -- [所有index的list]
        Raises:
            ValueError -- [description]
        """
        if self.is_empty():
            print("ATTENTION: empty single linked list")
            return
        if data is None:
            raise ValueError('Please input the correct data instead of None')

        indices = []
        ind = 0
        cursor = self.head
        while cursor:
            if cursor.data == data:
                indices.append(ind)
                if not all_instead_first:
                    return ind
            cursor = cursor.next
            ind += 1
        return indices

    def get_first_index(self, data):
        """获取data对应的第一条索引
        Arguments:
            data {[type]} -- [description]
        Returns:
            [type] -- [description]
        Raises:
            ValueError -- [description]
        """
        if self.is_empty():
            print("ATTENTION: empty single linked list")
            return
        if data is None:
            raise ValueError('Please input the correct data instead of None')
        return self.get_all_index(data, all_instead_first=False)

    def to_list(self):
        res = []
        if self.is_empty():
            print("ATTENTION: empty single linked list")
        else:
            cursor = self.head
            while cursor:
                res.append(cursor.data)
                cursor = cursor.next
        return res

    def reverse(self):
        """链表翻转"""
        if self.is_empty():
            print("ATTENTION: empty single linked list")
            return
        pre_node = None
        cursor = self.head
        while cursor:
            tmp = cursor.next
            cursor.next = pre_node
            pre_node = cursor
            cursor = tmp
        self.head = pre_node

    def get_middle_node(self, print_flag=True):
        """获取链表中间节点(index_mid)
        偶数/奇数长度： left [0, index_mid], right = [index_mid+1, length-1]
        奇数长度： len(left) = len(right) + 1
        Keyword Arguments:
            print_flag {bool} -- [description] (default: {True})
        Returns:
            [singleLinkedList] -- [left(未裁剪，与head相同), 左链表]
                若需要裁剪left：
                    slow.next = None
                    left = self.head
                但是，会把self.head一起裁剪掉
            [singleLinkedList] -- [right, 左链表]
            [Node] -- [mid_node, 中间节点]
        """
        if self.is_empty():
            print("ATTENTION: empty single linked list")
            return
        fast = self.head
        slow = self.head
        index = 0
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            index += 1
        if print_flag:
            print('链表中间节点索引：{}, 链表长度：{}'.format(index, self.length))
        # 中间节点
        middle_node = slow
        # 右半部分链表
        right = slow.next
        'ATTENTION: left不要做裁剪，会直接裁剪掉self.head'
        return self.head, right, middle_node

    def deepcopy(self, head_node):
        """递归方法 -- 链表深拷贝
        Arguments:
            head_node: 'Node' {[头结点]} -- [description]
        """
        head = head_node if isinstance(head_node, Node) else Node(head_node)
        if head is None:
            return None
        node = Node(head.data, None)
        node.next = self.deepcopy(head.next) if head.next else None
        return node

    @staticmethod
    def view(list_node, node_type=Node):
        """ 查看列表中的所有元素 """
        if not isinstance(list_node, node_type):
            raise AttributeError("Node type of input is expected")
        link_str = ''
        while list_node is not None:
            if list_node.next is not None:
                link_str += str(list_node.data) + '-->'
            else:
                link_str += str(list_node.data)
            list_node = list_node.next
        print('The linked list is: {}'.format(link_str))


if __name__ == '__main__':
    class NodeRandom:
        def __init__(self, x, next=None, random=None):
            self.data = int(x)
            self.next = next
            self.random = random

        def __repr__(self):
            return str(self.data)

    def deepcopy_with_random(head_node):
        """带随机指针的链表深拷贝
        思路：深拷贝， 新旧节点交替，完善random指针引用, 拆链(A.random=B, 则A'.random=B')
        Arguments:
            head_node {[NodeRandom]} -- [头结点]
        Returns:
            {[LinkedList]} -- [带随机指针的链表深拷贝的副本]
        """
        head = head_node if isinstance(
            head_node, NodeRandom) else NodeRandom(head_node)
        if not head:
            return None

        # Step-1: 遍历链表，获得新旧交替连接的新链表
        cursor = head
        while cursor:
            # 1. 复制节点，并重新引用链接
            link = NodeRandom(cursor.data, None, None)
            link.next = cursor.next
            cursor.next = link
            # 3. 移动cursor指针到步骤1中保存的节点
            cursor = link.next

        # Step-2: 遍历Step-1创建的新旧交替链表，完善复制节点的random指针引用
        cursor = head
        while cursor:
            # A.random=B, 则A'.random=B' （其中B'=A.random.next）
            cursor.next.random = cursor.random.next if cursor.random else None
            # 移动指针：跳过副本节点，只遍历原有链表的节点
            cursor = cursor.next.next

        # Step-3: 拆链表，获得原始链表和副本结点构成的新链表
        old_cursor = head
        new_cursor = head.next
        root = head.next
        while old_cursor:
            # 更改 原始链表 和 副本链表 的指针 （新链表时构建的链表的尾节点，需要判断None）
            old_cursor.next = old_cursor.next.next
            new_cursor.next = new_cursor.next.next if new_cursor.next else None
            # 移动指针：移动新旧指针cursor至对应链表的下一个结点 (右移)
            old_cursor = old_cursor.next
            new_cursor = new_cursor.next

        return root
