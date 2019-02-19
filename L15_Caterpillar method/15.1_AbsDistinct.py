# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 15：Caterpillar method
# P 15.1 AbsDistinct


def solution(A):
    """
    计算数组A中绝对值不同的数字的个数
    时间复杂度：O(N) or O(N*log(N))
    :param A: 数组
    :return: 绝对值不同的数字的个数
    """
    return len(set(abs(i) for i in A))

