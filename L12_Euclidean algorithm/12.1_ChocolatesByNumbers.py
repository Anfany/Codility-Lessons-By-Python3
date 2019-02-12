# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 12：Euclidean algorithm
# P 12.1 ChocolatesByNumbers


def solution_base(N, M):
    """
    N块巧克力排成一圈，从0号开始吃，每次间隔M-1个位置，可以吃到的巧克力的数量, 常规方法
    :param N: 巧克力数量
    :param M: 间隔的个数
    :return: 返回可以吃到的巧克力的数量
    """
    eat_dict = {}
    eat_count = 0
    if M == 1 or N == 1:
        return N
    while 1:
        sum_num = eat_count * M
        start_num = sum_num % N
        if start_num not in eat_dict:
            eat_count += 1
            eat_dict[start_num] = 1
        else:
            break
    return eat_count


def gcd(N, M):
    """
    计算N和M的最大公约数，利用欧几里得算法——辗转相除法
    :param N: 整数
    :param M: 整数
    :return: N和M的最大公约数
    """
    if N % M == 0:
        return M
    else:
        return gcd(M, N % M)


def solution(N, M):
    """
    N块巧克力排成一圈，从0号开始吃，每次间隔M-1个位置，可以吃到的巧克力的数量,时间复杂度O(log(N + M))
    首先计算N和M的最大公约数P, N除以P得到的商即为所求
    :param N: 巧克力数量
    :param M: 间隔的个数
    :return: 返回可以吃到的巧克力的数量
    """
    return int(N / gcd(N, M))
