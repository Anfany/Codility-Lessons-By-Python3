# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 3：Time Complexity
# P 3.1 FrogJump


def solution(X, Y, D):
    """
    每次跳跃D，从位置X到位置Y的最少的跳跃次数
    :param X: 起始位置
    :param Y: 目标位置
    :param D: 每次跳跃的距离
    :return: 最少次数
    """
    length = Y - X
    float_times = length / D
    int_times = int(float_times)
    if float_times > int_times:
        return int_times + 1
    else:
        return int_times