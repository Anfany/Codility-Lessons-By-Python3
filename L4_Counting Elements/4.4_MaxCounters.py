# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 4：Counting Elements
# P 4.4 MaxCounters


def solution_direct(N, A):
    """
    按照数组A中数字代表的规则，返回N个计数器的值序列，时间复杂度O(N*M)
    :param N: 计数器的个数
    :param A: 数组
    :return: 计数器值序列
    """
    counters_list = [0] * N
    for i in A:
        if i == N + 1:
            counters_list = [max(counters_list)] * N
        else:
            counters_list[i-1] += 1
    return counters_list

def solution_bad(N, A):
    """
    按照数组A中数字代表的规则，返回N个计数器的值序列，时间复杂度O(N*M)
    :param N: 计数器的个数
    :param A: 数组
    :return: 计数器值序列
    """
    sum_max = 0
    element_counter = {j: 0 for j in range(N)}
    for index, value in enumerate(A):
        if value != N+1:
            if value-1 in element_counter:
                element_counter[value-1] += 1
            else:
                element_counter[value-1] = 1
        else:
            sum_max += max(element_counter.items(), key=lambda x: x[1])[1]
            element_counter = {j: 0 for j in range(N)}
    return [element_counter[j]+sum_max if j in element_counter else sum_max for j in range(N)]


def solution(N, A):
    """
    按照数组A中数字代表的规则，返回N个计数器的值序列，时间复杂度O(N+M)
    :param N: 计数器的个数
    :param A: 数组
    :return: 计数器值序列
    """
    sum_max = 0
    element_counter = {}
    for index, value in enumerate(A):
        if value != N+1:
            if value-1 in element_counter:
                element_counter[value-1] += 1
            else:
                element_counter[value-1] = 1
        else:
            try:
                sum_max += max(element_counter.items(), key=lambda x: x[1])[1]
            except ValueError:
                sum_max += 0
            element_counter = {}
    return [element_counter[j]+sum_max if j in element_counter else sum_max for j in range(N)]




print(solution(1, [2, 1, 1, 2, 1]))