# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 2：Arrays
# P 3.3 TapeEquilibrium


def solution_list(A):
    """
    返回数组2部分差的最小值，时间复杂度O(N * N)
    :param A: N个整数组成的数组
    :return: 差的最小值
    """
    sum_list = sum(A)
    sub_abs_value = []
    for i in range(1, len(A)):
        sub_abs_value.append(abs(sum_list - 2 * sum(A[:i])))

    return min(sub_abs_value)


def solution(A):
    """
    返回数组2部分差的最小值，时间复杂度O(N)
    :param A: N个整数组成的数组
    :return: 差的最小值
    """
    sum_value = sum(A)

    if len(A) == 2:
        first_sub_abs = abs(A[1] - A[0])
        return first_sub_abs
    else:
        sub_abs_list = []
        first_sum = 0
        for i in A[:-1]:
            first_sum += i
            sub_abs = abs(sum_value - 2 * first_sum)
            if sub_abs == 0:
                return 0
            sub_abs_list.append(sub_abs)
        return min(sub_abs_list)

