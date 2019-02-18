# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 14：Binary search algorithm
# P 14.2 MinMaxDivision


def get_blocks(A, compare_num):
    """
    如果最大数值为compare_num，整个A可以分为多少块
    :param A: 正整数数组
    :param compare_num: 目标数值
    :return: 块数
    """
    blocks = 0
    num_sum = 0
    for i in A:
        num_sum += i
        if num_sum > compare_num: # 大于目标数值
            num_sum = i
            blocks += 1  # 块数需要加1
    return blocks + 1   # 最后这几个数算作一个块


def solution(K, M, A):
    """
    将数组A分为连续的K块，使得所有块的和的最大值最小
    :param K: 块的个数
    :param M: 数组A中元素的最大值不大于此数
    :param A: 正整数数组
    :return: 大和的最小值
    """
    sum_num = sum(A)
    if K == 1:
        return sum_num
    else:
        max_num = max(A)
        if K >= len(A):
            return max_num
        else:
            while max_num <= sum_num:  # 因为和值的最小值为max_num，最大值为sum_num，采用二分法查找
                middle = int((sum_num - max_num) / 2) + max_num
                blocks_count = get_blocks(A, middle)
                if K >= blocks_count: # 需要分的块数再多点，因此减小middle
                    sum_num = middle - 1
                else:
                    max_num = middle + 1
            return max_num




