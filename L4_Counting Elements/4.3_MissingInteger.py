# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 4：Counting Elements
# P 4.3 MissingInteger


def solution(A):
    """
    返回数组A中未出现的最小的正整数
    :param A: 数组
    :return: 未出现的最小的正整数
    """
    x_dict = {i: 0 for i in A}
    length = len(x_dict)
    for i in range(1, len(x_dict) + 1):
        if i not in x_dict:
            return i
    return length + 1