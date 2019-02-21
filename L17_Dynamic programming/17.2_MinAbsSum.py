# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 17：Dynamic programming
# P 17.2 MinAbsSum


def zero_one_pack(weight, value, max_weight):  # 0-1背包
    """
    返回总重量不超过MW的前提下，可以获得的最大价值(在本问题中，因为价值和重量是一样的，因此也可看作获得最接近MW的重量)
    :param weight: 重量数组
    :param value: 价值数组
    :param max_weight: 最大的重量
    :return: 可以获得的最大重量
    """
    #  存储最大价值的一维数组
    value_list = [0] * (max_weight + 1)
    # 开始计算
    for ii in range(len(weight)):  # 从第一个物品
        copy_value = value_list.copy()
        for jj in range(max_weight + 1):  # 从重量0
            if jj >= weight[ii]:  # 如果剩余的重量大于物品重量
                copy_value[jj] = max(value_list[jj - weight[ii]] + value[ii], value_list[jj])  # 选中第ii个物品和不选中，取大的
        value_list = copy_value.copy()  # 更新
    return value_list[-1]


def solution_zero_one(A):
    """
    针对数组A，寻找一个由1和-1组成的数组，使得两个数组对应元素乘积和的绝对值最小
    转化为01背包问题，时间复杂度：:O(N**2 * max(abs(A)))
    :param A: 数组A
    :return: 返回最小的绝对值
    """
    A = [abs(i) for i in A]  # 将数组A的全部元素转为非负数
    sum_num = sum(A)  # 数组A的元素之和
    max_weight = sum_num // 2  # 将数组A分为2部分，每一部分的和值需要最接近这个值
    max_sum = zero_one_pack(A, A, max_weight)  # 价值数组就是重量数组，获得最大价值就是获得最接近max_weight的最大重量
    return sum_num - 2 * max_sum

################################################################################


def multiple_pack(weight, value, count, max_weight):  # 多重背包
    # 存储最大价值的一维数组
    value_list = [0] * (max_weight + 1)
    # 开始计算
    for ii in range(len(weight)):  # 从第一个物品
        copy_value = value_list.copy()
        for jj in range(max_weight + 1):  # 从重量0
            if jj >= weight[ii]:  # 如果剩余的重量大于物品重量
                for gg in range(count[ii] + 1):  # 限制数量
                    if gg * weight[ii] <= jj:
                        copy_value[jj] = max(value_list[jj - gg * weight[ii]] + gg * value[ii], copy_value[jj])
        value_list = copy_value.copy()  # 更新
    return value_list[-1]


def solution_multiple(A):
    """
    针对数组A，寻找一个由1和-1组成的数组，使得两个数组对应元素乘积和的绝对值最小
    转化为多重背包问题，时间复杂度：:O(N**2 * max(abs(A)))
    :param A: 数组A
    :return: 返回最小的绝对值
    """
    A = [abs(i) for i in A]  # 将数组A的全部元素转为非负数
    weight = list(set(A))
    value = list(set(A))
    count = [A.count(j) for j in weight]
    sum_num = sum(A)  # 数组A的元素之和
    max_weight = sum_num // 2  # 将数组A分为2部分，每一部分的和值需要最接近这个值
    max_sum = multiple_pack(weight, value, count, max_weight)
    return sum_num - 2 * max_sum

#########################################################################


def solution_normal(A):
    """
    针对数组A，寻找一个由1和-1组成的数组，使得两个数组对应元素乘积和的绝对值最小
    时间复杂度：:O(N**2 * max(abs(A)))
    :param A: 数组A
    :return: 返回最小的绝对值
    """
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return abs(A[0])

    A = [abs(i) for i in A]  # 将数组A的元素转为非负数
    sum_num = sum(A)

    sign = [0] * (sum_num // 2 + 1)  # 存储否可以达到数值的标识，不大于S/2

    for j in A:
        if j <= sum_num // 2:  # 只有小于等于S/2的才计算
            sign_copy = sign.copy()  # 防止同一个数重复加
            for h in range(len(sign)):
                if sign[h] == 1:
                    try:
                        sign_copy[h + j] = 1
                    except IndexError:
                        pass
            sign_copy[j] = 1
            sign = sign_copy.copy()

    for k in range(sum_num // 2, -1, -1):  # 从大到小开始，只要能达到，就返回
        if sign[k] == 1:
            return sum_num - 2 * k

################################################################################


def solution(A):
    """
    针对数组A，寻找一个由1和-1组成的数组，使得两个数组对应元素乘积和的绝对值最小
    时间复杂度：:O(N * max(abs(A))**2)
    :param A: 数组A
    :return: 返回最小的绝对值
    """
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return abs(A[0])

    A = [abs(i) for i in A]  # 将数组A的元素转为非负数
    max_num = max(A)
    sum_num = sum(A)
    count = [0] * (max_num + 1)
    for i in range(len(A)):  # 统计每个元素出现的次数
        count[A[i]] += 1

    sign = [0] + [-1] * sum_num  # 存储从0到最大值中的每个值是否可以达到的标识

    for h in range(1, max_num + 1):
        if count[h] > 0:  # 说明有这个数
            for j in range(sum_num):
                if sign[j] >= 0:   #
                    sign[j] = count[h]
                elif j >= h and sign[j - h] > 0:  # 说明数字j也可以得到，但是之前未达到
                    sign[j] = sign[j - h] - 1  # 从h到达j消耗了一个j-h

    for i in range(sum_num // 2, -1, -1):  # 需要最接近sum_num // 2
        if sign[i] >= 0:  # 说明i这个数可以达到
            return sum_num - 2 * i








