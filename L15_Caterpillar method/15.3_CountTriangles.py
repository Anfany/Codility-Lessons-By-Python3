# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 15：Caterpillar method
# P 15.3 CountTriangles


def solution(A):
    """
    返回数组A的元素可以构成三角形的个数。
    :param A: 数组
    :return: 构成三角形的个数
    """
    #  首先将A进行排序
    A.sort()
    count_triangle = 0
    for index, value in enumerate(A):
        middle_idx = index + 1
        biggest_idx = index + 2
        while biggest_idx < len(A):
            if value + A[middle_idx] > A[biggest_idx]:  # 此时可以构成三角形
                count_triangle += biggest_idx - middle_idx  # 最大值到中间值之间的均能构成三角形
                biggest_idx += 1  # 增大最大值
            elif middle_idx < biggest_idx - 1:  # 够不成三角形，如果中间值较小，则试着增加中间值
                middle_idx += 1
            else:  # 如果中间值没有增加的余地，则同时增加中间值，和最大值。因为只增加最大值，还是够不成三角形
                biggest_idx += 1
                middle_idx += 1

    return count_triangle


