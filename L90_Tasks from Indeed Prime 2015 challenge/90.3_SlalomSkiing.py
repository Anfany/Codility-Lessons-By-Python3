# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 90：Tasks from Indeed Prime 2015 challenge
# P 90.3 SlalomSkiing


def longest_increasing_subsequence_dp(a):
    """
    利用动态规划算法，计算最长的递增子序列
    时间复杂度o(N**2)
    :param a: 数组a
    :return: 最长递增子序列的长度
    """
    length = len(a)
    save_max = [1] * length
    for i in range(1, length):
        for j in range(i):
            if a[i] > a[j] and save_max[j] + 1 > save_max[i]:
                save_max[i] = save_max[j] + 1
    return max(save_max)


def longest_increasing_subsequence_bs(a):
    """
    利用二分查找算法+动态规划，计算最长的递增子序列
    时间复杂度o(N*logN)
    :param a: 数组a
    :return: 最长递增子序列的长度
    """
    num_list = [-1, a[0]]   # 添加-1是为了二分查找的时候，要保证num_list[j-1]是存在的
    for i in a[1:]:
        if i > num_list[-1]:
            num_list.append(i)
        elif i < num_list[-1]:  # 使用二分查找算法，在num_list查找第一个不小于i的数，并替换之
            # 也就是寻找使得num_list[j-1] < i,并且num_list[j] >= i的j，然后令num_list[j] = i
            # 注意数组a中可能存在相同的元素
            start = 0
            end = len(num_list) - 1
            sign = 0
            middle = 0
            while start <= end:
                middle = int((start + end) / 2)
                if num_list[middle] < i:
                    start = middle + 1
                elif num_list[middle] > i:
                    end = middle - 1
                else:
                    sign = 1  # 恰好相等的时候
                    break
            if sign:
                num_list[middle] = i
            else:
                num_list[start] = i
    return len(num_list) - 1


def solution(A):
    """
    给定数组，找出最多可分解为三个单调部分的最长子序列
    :param A: 数组
    :return: 三个单调部分的最长子序列
    """
    max_num = max(A)   # 数组trans中会存在相同的元素
    trans = []
    for i in A:
        trans.append(max_num + max_num + i)
        trans.append(max_num + max_num - i)
        trans.append(i)
    return longest_increasing_subsequence_bs(trans)


