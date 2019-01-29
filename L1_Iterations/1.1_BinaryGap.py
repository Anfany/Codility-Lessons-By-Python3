# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 1：Iterations
# P 1.1 BinaryGap


def decimal_to_binary(N):
    """
    将十进制的正整数转为二进制表示
    :param N: 十进制的正整数
    :return: 二进制表示的字符串
    """
    binary = ''
    while N != 0:
        binary += str(N % 2)
        N = int(N / 2)
    return binary[::-1]


def solution(N):
    """
    在整数的二进制表示中查找最长的零序列
    :param N:1至2,147,483,647的整数
    :return: 最长的零序列的长度
    """
    binary_list = list(decimal_to_binary(N))
    if '0' not in binary_list:
        return 0
    elif binary_list.count('1') == 1:
        return 0
    else:
        first_1 = 0  # 前面1的位置
        max_length = 0  # 间隔长度
        for index, value in enumerate(binary_list):
            if value == '1':
                max_length = max(max_length, index-first_1-1)
                first_1 = index
        return max_length

