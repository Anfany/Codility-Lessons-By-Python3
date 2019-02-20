# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 16：Greedy algorithms
# P 16.2 TieRopes


def solution(A, B):
    """
    :param A: 线段的起始点集合
    :param B: 线段的终点集合，升序排列
    :return: 返回所有不重叠集中包含的线段数的最大值
    """
    if len(A) == 0:
        return 0
    count = 0
    end = B[0]
    for i in range(1, len(A)):
        if end < A[i]:
            count += 1
            end = B[i]
    return count + 1





