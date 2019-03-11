# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 99：Future training
# P 99.3 TreeHeight


def solution_(T):
    """
    返回二叉树T的最大深度，采用递归的方式
    :param T: 二叉树
    :return: 最大深度
    """
    # 二叉树为空树，层数就是0
    if T is None:
        return 0

    # 左子树的深度
    depth_left = solution_(T.l)
    # 右子树的深度
    depth_right = solution_(T.r)

    # 左、右子树深度较大的，然后加上1
    return max(depth_left, depth_right) + 1


def solution(T):
    """
    需要将最终的树的深度减去1
    :param T: 二叉树
    :return: 树的深度
    """
    return solution_(T)
