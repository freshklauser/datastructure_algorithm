# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/13 8:50
# @FileName : sort_integrate.py
# @SoftWare : PyCharm


class SortIntegrate(object):

    @staticmethod
    def bubble(seq):
        """
        反向遍历，两两比较，比较的同时伴随则数据交换
        :param seq:
        :return:
        """
        length = len(seq)
        for cur_len in range(length - 1, 0, -1):           # start = length - 1
            exchange = False
            for i in range(cur_len):
                if seq[i + 1] < seq[i]:
                    # exchange data each time when compared if later is lt
                    # former
                    seq[i], seq[i + 1] = seq[i + 1], seq[i]
                    exchange = True
            if not exchange:
                break
        return seq

    @staticmethod
    def select(seq):
        """
        两两对比，每次记录最大值位置，每趟遍历的最后一次比较时触发数据交换
        :param seq:
        :return:
        """
        length = len(seq)
        for cur_len in range(length - 1, 0, -1):        # start = length - 1
            position_swap = False
            marker = 0
            for i in range(
                    1, cur_len + 1):  # start = 1, end = cur_len + 1 (marker default is 0)
                # mark the index of larger value
                if seq[i] > seq[marker]:
                    marker = i
                    position_swap = True
                # consider data exchange when one loop end
                if marker != cur_len:
                    seq[i], seq[marker] = seq[marker], seq[i]
            if not position_swap:
                break
        return seq

    @staticmethod
    def insert(seq):
        """
        类比扑克，【有序列表 | 无序列表】
        正向遍历无序列表元素a(index:[1,...,length-1])，反向遍历有序列表进行对比，
        比a大的元素后移一位，直至碰到比a小的b，将a元素插入到b之后,跳出反向遍历
        :param seq:
        :return:
        """
        length = len(seq)
        for i in range(1, length):     # end = length - 1
            position = i
            target = seq[position]
            while position >= 1 and seq[position - 1] > target:
                seq[position] = seq[position - 1]
                position -= 1
            seq[position] = target
        return seq

    @staticmethod
    def sheller(seq):
        """
        间隔gap的数据为一组（逻辑分组，不是物理分组），间隔划分后的子列表个数=gap
        gap初始 n/2, 成倍递减 （n/4, n/8,.., 1）,针对每组插入排序
        最后针对所有数据执行一次插入排序
        :param seq:
        :return:
        """
        def gap_insert(seq, start, gap):
            for i in range(start + gap, len(seq), gap):
                position = i
                target = seq[i]
                while position >= gap and seq[position - gap] > target:
                    seq[position] = seq[position - gap]
                    position -= gap

                seq[position] = target

        length = len(seq)
        gap = length // 2
        while gap >= 1:
            for start_point in range(gap):
                gap_insert(seq, start_point, gap)
            gap //= 2
        return seq
