# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 6：Sorting
# P 6.2 MaxProductOfThree


def solution(A):
    """
    返回数组A中所有三元组对应的乘积的最大值,时间复杂度O(N * log(N))
    :param A: 整数数组
    :return: 乘积最大值
    """
    if len(A) == 3:
        return A[0] * A[1] * A[2]
    else:
        A.sort(reverse=True)
        if A[0] <= 0:
            return A[0] * A[1] * A[2]
        else:
            return max([A[0] * A[1] * A[2], A[0] * A[-1] * A[-2]])




