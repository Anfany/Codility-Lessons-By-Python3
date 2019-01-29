# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 9：Maximum slice problem
# P 9.1 MaxSliceSum


def solution(A):
    """
    返回序列A的子序列和的最大值
    :param A: 整数序列
    :return: 子序列和的最大值
    """
    if len(A) == 1:
        return A[0]
    else:
        max_num = max(A)  # 如果数组A中没有正数
        if max_num <= 0:
            return max_num
        else:
            sum_num = []  # 存储和值
            alive_sum = 0
            for i in A:
                if i < 0:
                    sum_num.append(alive_sum)
                alive_sum += i
                if alive_sum < 0:
                    sum_num.append(alive_sum - i)
                    alive_sum = 0
            sum_num.append(alive_sum)
            return max(sum_num)

