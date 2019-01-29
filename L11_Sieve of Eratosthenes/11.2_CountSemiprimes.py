# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 11：Sieve of Eratosthenes
# P 11.2 CountSemiprimes


def solution(N, P, Q):
    """
    返回由数组P、Q的元素组成的区间内，不大于N的半素数的个数, 时间复杂度O(N * log(log(N)) + M)
    :param N: 半素数的最大值
    :param P: 数组
    :param Q: 数组
    :return: 每次查询,得到的半素数的个数
    """
    #  半素数只有3或4个因子，并且不能是素数的立方，例如(1, 3, 9, 27)(1, 5, 25, 125)这种情况
    #  首先计算出不大于N的半素数列表
    semi_prime = []
    for i in range(1, N + 1):
        factor_count = 0
        sign = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                factor_count += 1
                f = i / j
                if f != j:
                    if f == j ** 2:
                        sign = 1
                        semi_prime.append(0)
                        break
                    else:
                        factor_count += 1
            if factor_count > 4:
                sign = 1
                semi_prime.append(0)
                break
        if sign != 1:
            if factor_count >= 3:
                semi_prime.append(i)
            else:
                semi_prime.append(0)

    index_dict = {}  # 得出当前数值以及前面一共有几个半素数
    semi_dict = {}  # 如果是半素数，则添加到字典中
    count = 0
    for index, value in enumerate(semi_prime):
        if value != 0:
            count += 1
            index_dict[value] = count
            semi_dict[value] = 0
        else:
            index_dict[index + 1] = count

    result_list = []  # 开始计算，在指定区间内有几个半素数
    for i, j in zip(P, Q):
        if i in semi_dict:
            result_list.append(index_dict[j] - index_dict[i] + 1)
        else:
            result_list.append(index_dict[j] - index_dict[i])

    return result_list

