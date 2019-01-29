# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 11：Sieve of Eratosthenes
# P 11.1 CountNonDivisible


def solution(A):
    """
    针对数组中的每一个元素，得到数组A中不是其因子数的个数, 时间复杂度O(N * log(N))
    :param A: 数组A
    :return: 返回每个元素的非因子数的个数序列
    """
    element_dict = {}
    for i in A:
        if i in element_dict:
            element_dict[i] += 1
        else:
            element_dict[i] = 1

    length = len(A)
    no_divided = []
    get_num = {}  # 用字典存储已经得到的非因子数个数，利用空间换时间
    for j in A:
        if j in get_num:
            no_divided.append(get_num[j])
        else:
            count_j_factor = 0
            for factor in range(1, int(j ** 0.5) + 1):
                if j % factor == 0:
                    if factor in element_dict:
                        count_j_factor += element_dict[factor]
                    other_factor = int(j / factor)
                    if other_factor != factor and other_factor in element_dict:
                        count_j_factor += element_dict[other_factor]
            no_divided_count = length - count_j_factor  # 非因子数等于所有的个数减去因子占的总个数
            no_divided.append(no_divided_count)
            get_num[j] = no_divided_count
    return no_divided



