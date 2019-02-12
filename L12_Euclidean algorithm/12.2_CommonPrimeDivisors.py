# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 12：Euclidean algorithm
# P 12.2 CommonPrimeDivisors


def prime(a, b):
    """
    返回正整数a的质因子集合
    :param a: 正整数
    :return: 返回质因子集合
    """
    start = 2
    while a != 1 and b != 1:
        if not a % start:
            if not b % start:
                while a - int(a) == 0:
                    a_num = a
                    a /= start

                while b - int(b) == 0:
                    b_num = b
                    b /= start

                a = a_num
                b = b_num
            else:
                break
        else:
            if not b % start:
                break
            else:
                start += 1

    if a == b:
        return True
    else:
        return False


def solution(A, B):
    """
    返回数组A和B组成的数对含有相同的质因子集合相同的个数,时间复杂度O(Z * log(max(A) + max(B))**2) or O(Z * (max(A) + max(B))**(1/2))
    :param A: 数组
    :param B: 数组
    :return: 返回相同的个数
    """
    count = 0
    for i, j in zip(A, B):
        if i == j:
            count += 1
        else:
            if prime(i, j):
                count += 1
    return count


