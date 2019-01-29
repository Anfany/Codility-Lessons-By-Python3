# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 8：Leader
# P 8.1 EquiLeader


def solution(A):
    """
    返回数组A中的超频数索引的个数
    :param A:  数组
    :return: 返回超频数索引的个数
    """
    leader_dict = {}
    for i in A:
        if i in leader_dict:
            leader_dict[i] += 1
        else:
            leader_dict[i] = 1
    # 确定超频数，以及出现的次数
    leader, times = max(leader_dict.items(), key=lambda x: x[1])

    equi_count = 0

    count = 0  # 超频数已经出现的次数
    length = len(A)
    for index, value in enumerate(A):
        if value == leader:
            count += 1
        if count > (index + 1) / 2 and (times - count) > (length - (index + 1)) / 2:
            equi_count += 1
    return equi_count





