# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 5：Prefix Sums
# P 5.3 MinAvgTwoSlice



def solution(A):
    """
    寻找所有切片中具有最小均值的起始位置，时间复杂度O(N)
    :param A: 数组
    :return: 起始位置
    """
    avg_dict = {}
    for index, value in enumerate(A[:-1]):
        avg1 = (value + A[index + 1]) / 2
        try:
            avg2 = (value + A[index+1] + A[index+2]) / 3
            min_avg = min(avg1, avg2)
            if min_avg not in avg_dict:
                avg_dict[min_avg] = index
        except IndexError:
            if avg1 not in avg_dict:
                avg_dict[avg1] = index

    return min(avg_dict.items(), key=lambda x: x[0])[1]


print(solution([4, 2, 2, 5, 1, 5, 8]))