# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 13：Fibonacci numbers
# P 13.2 Ladder


def ladder(n):
    """
    计算爬到横档数为n的梯子的顶端的方式的个数
    :param n: 梯子的横档数
    :return: 爬的方式的个数
    """
    methods = [1] * (n + 1)  # 横档数n：方式个数
    methods[1] = 2
    for i in range(2, n+1):
        methods[i] = methods[i-1] + methods[i-2]
    return methods


def solution_normal(A, B):
    """
    数组A的元素为梯子的横档数，数组B元素为计算mod值得幂数，时间复杂度为O(L**2)
    :param A: 正整数数组
    :param B: 正整数数组
    :return: mod值的数组
    """
    max_num = len(A)
    methods_dict = ladder(max_num)
    C = [2 ** h for h in B]
    return [methods_dict[i-1] % j for i, j in zip(A, C)]


def solution(A, B):
    """
    数组A的元素为梯子的横档数，数组B元素为计算mod值得幂数，时间复杂度为O(L)
    :param A: 正整数数组
    :param B: 正整数数组
    :return: mod值的数组
    """
    max_num = len(A)
    methods_dict = ladder(max_num)
    C = [2 ** h for h in B]
    return [methods_dict[i-1] & (j - 1) for i, j in zip(A, C)]
