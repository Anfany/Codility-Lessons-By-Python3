# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 15：Caterpillar method
# P 15.2 CountDistinctSlices


def computer(start, end):
    """
    计算从start到end开始，连续组合的个数
    :param start: 起始点
    :param end: 终点
    :return: 返回所有连续组合的个数
    start：2
    end:4
    连续的组合分别为(2, 3), (2, 4), (3, 4)
    因此返回3
    """
    return int((end - start + 1) * (end - start + 1 - 1) / 2)


def solution(M, A):
    """
    返回数组A中所有不同切片的个数
    :param M: 数组A中的元素的最大值不大于此数
    :param A: 数组
    :return: 数组不同切片的个数
    """
    sum_times = len(A)  # 每个元素构成的切片都是不同切片
    existed = {}
    start = 0  # 计算不同切片个数的起始索引
    end = 0
    for index, value in enumerate(A):
        end = index
        if value in existed:
            if existed[value] >= start:
                sum_times += computer(start, index-1)
                sum_times -= computer(existed[value] + 1, index-1)  # 减去下一次计算会重复的部分
                start = existed[value] + 1  # 更新起始索引
                if sum_times >= 1e9:
                    return 1000000000
        existed[value] = index
    sum_times += computer(start, end)
    return min(sum_times, 1000000000)




