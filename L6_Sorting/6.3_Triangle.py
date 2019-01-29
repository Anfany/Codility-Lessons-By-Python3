# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 6：Sorting
# P 6.3 Triangle


def solution(A):
    """
    判断数组中的任何三元组对应的三个数是否是三角形的,时间复杂度为O(N*log(N))
    :param A: 数组
    :return: 返回结果
    """
    if len(A) < 3:
        return 0
    else:
        A.sort(reverse=True)
        for index, value in enumerate(A[:-2]):
            if A[index+2] <= 0:
                return 0
            else:
                if value < A[index+1] + A[index+2]:
                    return 1
        return 0
