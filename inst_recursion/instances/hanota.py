# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/23 18:03
# @FileName : hanota.py
# @SoftWare : PyCharm

"""
汉诺塔问题： 移动盘片
盘片位置： left, middle, right
盘片个数： number
描述：从 left 移动到 right
    left 盘片从上到下依次从小到大叠放
过程：
    (1) 上面的 N-1 个盘片  left  --> right --> middle
    (2) 最底层的  N   盘片   left  --> right
    (3) 中间的 N-1 个盘片 middle --> left --> right
"""


def hanota_tower_move(height, org_tower, mid_tower, target_towerl):
    """
    移动高度为height的汉诺塔，从org_tower,经由mid_tower,移动到target_tower
    :param height: 高height的汉诺塔
    :param org_tower:
    :param mid_tower:
    :param target_pole:
    :return:
    """
    if height >= 1:
        # 移动上层 N-1 层的汉诺塔, org --> mid --> target
        hanota_tower_move(height - 1, org_tower, target_towerl, mid_tower)
        # 移动第N层的盘片
        disk_move(height, org_tower, target_towerl)
        # 移动上层 N-1 层的汉诺塔，mid --> org --> target
        hanota_tower_move(height - 1, mid_tower, org_tower, target_towerl)


def disk_move(height, org_tower, target_tower):
    print("Moving disk[{}] From '{}' move to '{}'".format(height, org_tower, target_tower))


if __name__ == '__main__':
    height = 6
    org = 'O'
    mid = 'M'
    target = 'T'
    hanota_tower_move(height, org, mid, target)
