# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 5：Prefix Sums
# P 5.4 CountDiv



def solution_direct(A, B, K):
    """
    计算区间[A,B]内可以被K整除的整除的个数，时间复杂度O(B-A)
    :param A: 数
    :param B: 数
    :param K: 除数
    :return: 起始位置
    """
    sign = 0
    for i in range(A, B + 1):
        if i % K == 0:
            sign += 1
    return sign


def solution(A, B, K):
    """
    计算区间[A,B]内可以被K整除的整除的个数，时间复杂度O(B-A)
    :param A: 数
    :param B: 数
    :param K: 除数
    :return: 起始位置
    """
    return B // K - A // K + (not A % K)
