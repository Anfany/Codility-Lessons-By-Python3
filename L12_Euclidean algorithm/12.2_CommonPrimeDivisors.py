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
            if not b % start:  # a,b相同的质因子start
                a_num = a
                b_num = b
                while a - int(a) == 0:  # 把相同的质因子一次性删除
                    a_num = a
                    a /= start
                while b - int(b) == 0:  # 把相同的质因子一次性删除
                    b_num = b
                    b /= start
                a = a_num
                b = b_num
            else:  # a能被start整除，b不能
                break
        else:
            if not b % start:  # b能被start整除，a不能
                break
            else:  # 都不能被start整除
                start += 1
    if a == b:
        return True
    else:
        return False


def solution_base(A, B):
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

#########################################


def gcd(a, b):
    """
    计算a和b的最大公约数，利用欧几里得算法——辗转相除法
    :param a: 整数
    :param b: 整数
    :return: a和b的最大公约数
    """
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def judge(a, b):
    """
    判断a中是否存在b中不存在的因子
    :param a: 正整数
    :param b: 正整数
    :return: 存在返回True，不存在返回False
    """
    p = gcd(a, b)
    while p != 1:
        a //= p
        p = gcd(a, b)
    if a == 1:
        return False
    else:
        return True


def solution(A, B):
    """
    返回数组A和B组成的数对含有相同的质因子集合相同的个数
    首先得到A和B的最大公约数P，然后再判断A、B中是否存在P中不存在的因数， 时间复杂度O(Z * log(max(A) + max(B))**2)
    :param A: 数组
    :param B: 数组
    :return: 返回相同的个数
    """
    count = 0
    for i, j in zip(A, B):
        if i == j:
            count += 1
        else:
            p = gcd(i, j)
            # 判断A、B中是否存在P中不存在的因数
            if not judge(i, p) and not judge(j, p):
                count += 1
    return count


