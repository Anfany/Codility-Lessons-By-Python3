# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 3：Time Complexity
# P 3.2 PermMissingElem


def solution(A):
    """
    返回数组A中缺失的元素
    :param A: 一个由1到N+1中的N个不同的整数组成的数组
    :return: 缺失的元素
    """
    index_dict = {index+1: value for index, value in enumerate(A)}
    value_dict = {value: index+1 for index, value in enumerate(A)}
    for k in index_dict:
        if k not in value_dict:
            return k
    return len(A) + 1

