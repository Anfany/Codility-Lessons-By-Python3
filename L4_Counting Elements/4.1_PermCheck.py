# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 4：Counting Elements
# P 4.1 PermCheck


def solution(A):
    """
    判断数组是否是一个排列, 时间复杂度O(N) or O(N * log(N))
    :param A: N个整数组成的数组
    :return: 是排列返回1，不是返回0
    """
    if sorted(A) == list(range(1, len(A)+1)):
        return 1
    else:
        return 0

