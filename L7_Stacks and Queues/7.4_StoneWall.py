# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 7：Stacks and Queues
# P 7.4 StoneWall


def solution(H):
    """
    返回构成石墙H，所需要的最小的矩形石块的个数
    :param H: 代表石墙的高度数组
    :return: 返回矩形石块的个数
    """
    stone_count = 0
    stone_list = []
    for i in H:
        while len(stone_list) != 0 and stone_list[-1] > i:
            stone_list.pop(-1)
            stone_count += 1
        if len(stone_list) == 0 or i > stone_list[-1]:
            stone_list.append(i)
    stone_count += len(stone_list)

    return stone_count

