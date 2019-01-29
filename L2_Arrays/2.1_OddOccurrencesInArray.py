# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 2：Arrays
# P 2.1 OddOccurrencesInArray


def solution_list(A):
    """
    寻找数组A中出现的次数为奇数的元素,O(N**2)
    :param A: 列表形式数组
    :return: 元素
    """
    number_only = list(set(A))
    for i in number_only:
        if A.count(i) % 2 == 1:
            return i


def solution(A):
    """
    寻找数组A中出现的次数为奇数的元素,O(N) or O(N*log(N))
    :param A: 列表形式数组
    :return: 元素
    """
    times_dict = {}
    for i in A:
        if i in times_dict:
            times_dict[i] += 1
        else:
            times_dict[i] = 1
    for k in times_dict:
        if times_dict[k] % 2 == 1:
            return k