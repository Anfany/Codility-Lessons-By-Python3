# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 99：Future training
# P 99.2 SocksLaundering


def solution(S):
    """
    判断字符串S是否是中心对称的
    :param S: 字符串
    :return: 返回中心字符的下标或者-1
    """
    length = len(S)
    if length % 2 == 0:
        return -1
    if length == 1:
        return 0
    center = length // 2
    if S[:center][::-1] == S[center+1:]:
        return center
    else:
        return -1