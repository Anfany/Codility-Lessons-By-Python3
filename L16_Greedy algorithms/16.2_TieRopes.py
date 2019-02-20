# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 16：Greedy algorithms
# P 16.2 TieRopes


def solution(K, A):
    """
    通过系住相邻的绳索，使得最终满足长度条件的绳索数最大
    时间复杂度：O(N)
    :param K: 最终绳索的长度的最小值
    :param A: 绳索的长度
    :return: 满足条件的绳索数的最大值
    """
    count = 0
    length = 0
    for i in A:
        if i >= K:
            length = 0
            count += 1
        else:
            length += i
            if length >= K:
                length = 0
                count += 1
    return count


