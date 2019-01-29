# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 5：Prefix Sums
# P 5.2 GenomicRangeQuery


def solution_direct(S, P, Q):
    """
    按照数组给定的范围，返回字符串S在这个范围内对应的最小的数, 时间复杂度O(N * M)
    :param S: 代表基因序列的字符串
    :param P: 表示范围的数组
    :param Q: 表示范围的数组
    :return: 每一次查询的结果组成的列表
    """
    impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    result = []
    for i, j in zip(P, Q):
        result.append(impact_factor[min(list(S[i: j+1]))])
    return result



def next_occur(S, X):
    """
    计算字符串S中，对于核苷酸X，下一个出现该核苷酸的索引，如果当前是X，则索引为当前的索引
    :param S: DNA字符串
    :param X: 核苷酸
    :return: 所以序列
    """
    index_list =[-1] * len(S)
    for index, value in enumerate(S[::-1]):  # 注意字符串反转
        if value == X:
            index_list[index] = len(S) - index - 1
        else:
            index_list[index] = index_list[index-1]
    return index_list[::-1]


def solution(S, P, Q):
    """
    按照数组给定的范围，返回字符串S在这个范围内对应的最小的数,时间复杂度O(N + M)
    :param S: 代表基因序列的字符串
    :param P: 表示起始位置的数组
    :param Q: 表示结束位置的数组
    :return: 每一次查询的结果组成的列表
    """
    result = []
    factor_list = ['A', 'C', 'G', 'T']
    all_index_list = [next_occur(S, j) for j in factor_list]
    for i in range(len(P)):
        for j in range(len(factor_list)):
            if all_index_list[j][P[i]] <= Q[i] and all_index_list[j][P[i]] != -1:
                result.append(j + 1)
                break
    return result

