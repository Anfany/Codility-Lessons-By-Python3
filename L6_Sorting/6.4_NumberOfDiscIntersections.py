# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 6：Sorting
# P 6.4 NumberOfDiscIntersections


def solution_set(A):
    """
    返回数组A代表的圆盘中，相交圆盘的个数,时间复杂度O(N**2)
    :param A: 数组
    :return: 相交圆盘的个数
    """
    limit = []
    length = len(A)
    for index, value in enumerate(A):
        limit.append([max(0, index-value), min(length, index+value)])
    count = 0
    for index, value in enumerate(limit[: -1]):
        for j in limit[index:]:
            if value[0] <= j[0] <= value[1] or j[0] <= value[0] <=j[1]:
                count += 1
    return count


def solution_direct(A):
    """
    返回数组A代表的圆盘中，相交圆盘的个数，时间复杂度O(N**2)
    :param A: 数组
    :return: 相交圆盘的个数
    """
    count = 0
    for index_i, value_i in enumerate(A[:-1]):
        for index_j, value_j in enumerate(A[index_i+1:]):
            if value_i + value_j >= index_j + index_i + 1 - index_i:
                count += 1
    return count


def binary_search(ex_list, ex_num):
    """
    实现二分查找算法，获得ex_num不小于数组ex_list中的元素的个数。适用于ex_num不存在于ex_list中的情况
    :param ex_list: 数组
    :param ex_num: 数值
    :return: 元素的个数
    """
    start = 0
    end = len(ex_list) - 1
    if ex_num <= ex_list[0]:
        return start + 1
    elif ex_num >= ex_list[-1]:
        return end + 1
    else:
        while 1:
            center = (start + end) // 2
            if ex_list[center] > ex_num:
                end = center - 1
            elif ex_list[center + 1] < ex_num:
                start = center + 2
            else:
                return center + 1


def solution(A):
    """
    返回数组A代表的圆盘中，相交圆盘的个数，时间复杂度O(N*log(N)) or O(N)
    :param A: 数组
    :return: 相交圆盘的个数
    """
    count = 0
    i_limit = []
    j_limit = []
    for index, value in enumerate(A):
        i_limit.append(value + index)
        j_limit.append(index - value)
    #  针对i_limit中的每个元素，利用二分查找算法，找到其不小于j_limit中元素的个数
    j_limit.sort()  # 二分法要求数组是有序的
    for ind, val in enumerate(i_limit[:-1]):
        count += max(binary_search(j_limit, val+0.1) - 1 - ind, 0)
        # 因为i=j时，A[i]+i 肯定不小于j-A[j],也就是说多算了一个，因此要减去1。
        # val之所以加上0.1，因为数组j_limit中都是整数，并且有的整数有多个，这么设置是为了得到最后一个val出现的位置。
        # 减去ind是因为圆盘A和圆盘B相交，次数加上1了，圆盘B和圆盘A相交就不用再加1了。
        if count > 10000000:
            return -1
    return count

