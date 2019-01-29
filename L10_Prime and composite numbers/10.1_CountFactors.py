# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 10：Prime and composite numbers
# P 10.1 CountFactors


def solution(N):
    """
    返回N的所有因子的个数,时间复杂度O(sqrt(N))
    :param N: 正整数N
    :return: 返回N的所有因子的个数
    """
    factor_dict = {}
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            if i not in factor_dict:
                factor_dict[i] = 0
            j = N / i
            if j == int(j) and j not  in factor_dict:
                factor_dict[j] = 0
    return len(factor_dict)




