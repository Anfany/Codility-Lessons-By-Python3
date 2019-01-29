# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 10：Prime and composite numbers
# P 10.3 Peaks


def factor_no_one(N, p_count):
    """
    返回N的所有因子, 大于1，不大于P_count的因子序列
    :param N: 正整数N，大于等于2
    :param p_count: 峰值的个数
    :return: 返回N的所有不为1，并且不大于p_count的因子
    """
    factor_dict = {}
    for i in range(2, min(int(N ** 0.5), p_count) + 1):
        if N % i == 0 :
            if i not in factor_dict:
                factor_dict[i] = 0
            j = N / i
            if j == int(j) and int(j) not in factor_dict and j <= p_count:
                factor_dict[int(j)] = 0
    return list(factor_dict.keys()) + [N]


def solution(A):
    """
    将数组A切割成同等元素个数的块的最大个数,时间复杂度O(N * log(log(N)))
    :param A: 数组
    :return: 最大块数
    """
    peaks_list = []
    for index, value in enumerate(A):
        if index != 0:
            try:
                if value > A[index - 1] and value > A[index + 1]:
                    peaks_list.append(index)
            except IndexError:
                break
    length = len(peaks_list)  # 峰值的个数
    if length == 0:
        return 0
    elif length == 1:
        return 1
    else:
        length_a = len(A)  # 数组中所有元素的个数
        factor_list = factor_no_one(length_a, length)  # 元素个数的因子序列
        block_list = [1]  # 存储可能的块数
        for i in factor_list:
            #  每个块含有的元素的个数
            block_count = int(length_a / i)
            #  判断是否每个块都会有峰值
            blocks = [0] * i
            for j in peaks_list:
                blocks[j // block_count] = 1
            if 0 not in blocks:
                block_list.append(i)
        return max(block_list)







