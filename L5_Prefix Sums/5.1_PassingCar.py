# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 5：Prefix Sums
# P 5.1 PassingCars


def solution(A):
    """
    根据数组A中车的行驶方向，确定出现多少对过路车
    :param A: 数组
    :return: 过路车的对数
    """
    reverse_list = A[::-1]
    pairs = 0
    forward_passing = 0
    zero_sign = 0
    for index, value in enumerate(reverse_list):
        if value == 0:
            forward_passing += index - zero_sign
            pairs += forward_passing
            zero_sign = index + 1
            if pairs > 1000000000:
                return -1
    return pairs