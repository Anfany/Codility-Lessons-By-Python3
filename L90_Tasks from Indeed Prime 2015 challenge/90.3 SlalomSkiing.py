# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 90：Tasks from Indeed Prime 2015 challenge
# P 90.3 SlalomSkiing



def longest_increasing_subsequence_dp(a):
    """
    利用动态算法计算，最长的递增子序列
    :param a: 数组a
    :return: 最长递增子序列的长度
    """
    length = len(a)
    save_max = [1] * length
    for i in range(length-1):
        for j in range(i+1, length):
            if a[i] > a[j] and save_max[j] + 1 > save_max[i]:
                save_max[i] = save_max[j] + 1
    return max(save_max)


print(longest_increasing_subsequence_dp([1, 4, 5, 6, 3, 3, 2, 34, 455, 55, 59]))


def solution(A):
    """
    给定数组，找出最多可分解为三个单调部分的最长子序列
    :param A: 数组
    :return: 三个单调部分的最长子序列
    """
    max_num = max(A)
    trans = []
    for i in A:
        trans.append(max_num + max_num + i)
        trans.append(max_num + max_num - i)
        trans.append(i)
    return longest_increasing_subsequence_dp(trans)

