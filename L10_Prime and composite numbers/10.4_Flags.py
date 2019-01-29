# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 10：Prime and composite numbers
# P 10.4 Flags


def solution(A):
    """
    数组A代表的山峰高度的山上，可以设置旗标的最大个数,时间复杂度O(N)

    :param A: 数组
    :return: 旗标的最大个数
    """
    peaks_list = []  # 存储峰值的序列
    for index, value in enumerate(A):
        if index != 0:
            try:
                if value > A[index - 1] and value > A[index + 1]:
                    peaks_list.append(index)
            except IndexError:
                break

    if len(peaks_list) == 0:
        return 0
    elif len(peaks_list) == 1:
        return 1
    else:
        max_k = int((peaks_list[-1] - peaks_list[0]) ** 0.5 + 1)   # 理论上可以带的最大旗标数
        for i in range(max_k, 1, -1):
            address_flag = [peaks_list[0]]
            for val in peaks_list[1:]:
                if val - address_flag[-1] >= i:
                    address_flag.append(val)
                    if len(address_flag) >= i:
                        return i
        return 1









