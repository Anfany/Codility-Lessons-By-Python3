# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 9：Maximum slice problem
# P 9.3 MaxDoubleSliceSum


def solution(A):
    """
    返回数组A的所有双切片中的和的最大值
    :param A: 数组
    :return: 返回双切片的和的最大值
    """
    length = len(A)
    if length == 3 or max(A) <= 0:
        return 0

    #  正向遍历
    forward_max = [0] * length
    for index, value in enumerate(A[1:-1]):
        forward_max[index + 1] = max(forward_max[index] + value, 0)

    reverse_max = [0] * length
    for index, value in enumerate(A[::-1][1:-1]):
        reverse_max[index + 1] = max(reverse_max[index] + value, 0)

    reverse_max = reverse_max[::-1]

    combine_max = []
    for i in range(1, length - 1):
        combine_max.append(forward_max[i - 1] + reverse_max[i + 1])
    return max(combine_max)



