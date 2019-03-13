# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 99：Future training
# P 99.4 ArrayInversionCount


def solution_direct(A):
    """
    返回数组A中逆序索引对的个数
    时间复杂度O(N**2)
    :param A: 数组
    :return: 逆序索引对的个数
    """
    return len([0 for i in range(len(A)) for j in range(i, len(A)) if A[i] > A[j]])


def merge(a):
    """
    实现归并排序
    :param a:数组
    :return:逆序索引对的个数
    """
    # 总的逆序索引对的个数
    length = len(a)
    if length <= 1:
        return a, 0
    # 分割点
    middle = length // 2
    # 左边
    left_list, left_count = merge(a[: middle])
    # 右边
    right_list, right_count = merge(a[middle:])
    # 左右之和
    count = left_count + right_count
    # 合并在一起的序列，也就是排序后的系列
    sorted_list = []
    #  合并时候的逆序数
    while len(left_list) and len(right_list):
        if left_list[0] > right_list[0]:
            len_left = len(left_list)
            count += len_left
            small = right_list.pop(0)
            sorted_list.append(small)
        else:
            small = left_list.pop(0)
            sorted_list.append(small)

    if left_list:
        sorted_list += left_list
    else:
        sorted_list += right_list
    return sorted_list, count


def solution(A):
    """
    返回数组A中逆序索引对的个数
    利用归并排序的思想，最终的逆序数对的个数=左序列排完序得到的逆序数+右序列排完序得到的逆序数+合并左右得到的逆序数
    其实所有的逆序数归根结底都是合并左右得来的逆序数
    时间复杂度：O(N*log(N))
    :param A: 数组
    :return: 逆序索引对的个数
    """
    length = len(A)
    if length <= 1:
        return 0
    count = merge(A)[1]
    if count > 1e9:
        return -1
    return count








