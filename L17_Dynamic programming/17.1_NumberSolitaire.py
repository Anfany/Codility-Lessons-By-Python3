# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 17：Dynamic programming
# P 17.1 NumberSolitaire


def solution(A):
    """
    计算数组A中，索引差不大于6的数字构成的集合中，和值的最大值
    :param A: 数组
    :return: 和值绝对值的最大值
    """
    max_num_list = [A[0]]
    for value in A[1:-1]:
        if len(max_num_list) < 6:
            max_num_list.append(max(max_num_list) + value)
        else:
            max_num_list.append(max(max_num_list) + value)
            max_num_list.pop(0)
    return max(max_num_list) + A[-1]





