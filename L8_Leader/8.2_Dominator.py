# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 8：Leader
# P 8.2 Dominator


def solution(A):
    """
    判断数组A是否存在支配数，存在返回其任何一个索引，否再返回-1
    :param A: 数组
    :return: 返回支配数的任何索引，或者-1
    """
    if len(A) == 0:
        return -1
    leader_dict = {}
    for i in A:
        if i in leader_dict:
            leader_dict[i] += 1
        else:
            leader_dict[i] = 1

    leader, times = max(leader_dict.items(), key=lambda x: x[1])

    if times > len(A) / 2:
        return A.index(leader)
    else:
        return -1