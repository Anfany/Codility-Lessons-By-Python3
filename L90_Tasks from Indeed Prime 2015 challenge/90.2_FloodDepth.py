# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 90：Tasks from Indeed Prime 2015 challenge
# P 90.2 FloodDepth


def judge_depth(hill):
    """
    寻找低洼区域，并返回最大水深
    低洼区域的定义：左峰高度小于右峰高度的视为低洼区域
    :param hill: 每一块山区的高度
    :return: 最大水深
    """
    max_depth = 0
    if len(hill) <= 1:
        return max_depth

    right_high = 0  # 判断是否是低洼区域

    start_height = hill[0]  # 开始的高度

    save_height = []  # 储存低洼区域的山区高度

    for h in hill[1:]:
        if start_height > h:  # 低洼区域的左峰出现
            right_high = 1
            save_height.append(h)
        else:   # 低洼区域的右峰出现
            if right_high:   # 并且左峰也有，此时计算这个低洼区域的最大水深
                max_depth = max(max_depth, start_height - min(save_height))
            start_height = h  # 重新定义低洼区域的左峰阈值
            right_high = 0
            save_height = []  # 重新定义储存低洼区域的山区高度
    return max_depth


def solution(A):
    """
    根据山区的高度，返回洪水过后这片山区蓄水的最大深度
    :param A: 每一块山区的高度
    :return: 最大水深
    """
    return max(judge_depth(A[::-1]), judge_depth(A))










