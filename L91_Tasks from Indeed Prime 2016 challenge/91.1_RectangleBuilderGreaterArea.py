# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 91：Tasks from Indeed Prime 2016 challenge
# P 91.1 RectangleBuilderGreaterArea


def solution(A, X):
    """
    利用数组A中的元素，构建面积不小于X的不同矩形的个数
    :param A: 数组
    :param X: 面积阈值
    :return: 满足条件的矩形的个数
    """
    count_item = {}
    for i in A:
        if i in count_item:
            count_item[i] += 1
        else:
            count_item[i] = 1

    no_less_than_2 = [j for j in count_item if count_item[j] >= 2]  # 出现次数大于等于2的存储下来

    ordered_list = sorted(no_less_than_2)  # 按照栅栏的长度升序排序

    length = len(ordered_list)  # 可用栅栏的个数

    if not length:  # 没有可用的栅栏
        return 0
    else:
        if length == 1:  # 只有一种长度的栅栏，只有栅栏数不小于4时，才可以建立围栏
            if count_item[ordered_list[0]] >= 4:
                return 1
            else:
                return 0
        else:
            sum_count = 0  # 记录总的个数
            for index, value in enumerate(ordered_list):
                if count_item[value] >= 4:
                    start = index    # 如果用一种长度的栅栏，其数量需要不小于4
                else:
                    start = index + 1
                end = length - 1
                #  开始二分查找算法
                while start <= end:
                    middle = int((start + end) / 2)
                    if ordered_list[middle] * value >= X:
                        end = middle - 1
                    else:
                        start = middle + 1
                sum_count += length - end - 1
                if sum_count > 1e9:
                    return -1
            return sum_count
