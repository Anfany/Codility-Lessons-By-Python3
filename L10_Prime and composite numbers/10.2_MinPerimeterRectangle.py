# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 10：Prime and composite numbers
# P 10.2 MinPerimeterRectangle


def solution(N):
    """
    返回面积为N的所有矩形的最小周长,时间复杂度O(sqrt(N))
    :param N: 正整数N
    :return: 返回矩形的最小周长
    """
    for i in range(int(N ** 0.5), 0, -1):
        if N % i == 0:
            return 2 * (i + int(N / i))

