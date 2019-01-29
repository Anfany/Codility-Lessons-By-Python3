# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 6：Sorting
# P 6.1 Distinct


def solution_one(A):
    """
    返回数组A中不同数值的个数，时间复杂度O(N*log(N)) or O(N)，利用Python函数set
    :param A: 整数数组
    :return: 不同值的个数
    """
    return len(set(A))


def solution(A):
    """
    返回数组A中不同数值的个数，时间复杂度O(N*log(N)) or O(N)，利用字典
    :param A: 整数数组
    :return: 不同值的个数
    """
    number_dict = {}
    sign = 0
    for j in A:
        if j not in number_dict:
            number_dict[j] = 0
            sign += 1
    return sign
