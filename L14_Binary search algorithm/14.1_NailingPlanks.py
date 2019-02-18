# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 14：Binary search algorithm
# P 14.1 NailingPlanks


def solution_worst(A, B, C):
    """
    数组A、B对应元素代表木板，C元素代表可以钉钉子的位置。计算钉牢所有木板需要的最小的钉子数量。
    一般解法：时间复杂度O((N + M) * N)
    :param A: 正整数数组
    :param B: 正整数数组
    :param C: 正整数数组
    :return: 最小的钉子数量
    """
    D = [0] * len(A)
    for index, value in enumerate(C):
        for i, j in enumerate(A):
            if j <= value <= B[i]:
                D[i] = 1
        if 0 not in D:
            return index + 1
    return -1


def solution_worse(A, B, C):
    """
    数组A、B对应元素代表木板，C元素代表可以钉钉子的位置。计算钉牢所有木板需要的最小的钉子数量。
    一般解法：时间复杂度O(N * M)
    :param A: 正整数数组
    :param B: 正整数数组
    :param C: 正整数数组
    :return: 最小的钉子数量
    """
    for index, value in enumerate(C):
        if A:
            DA = []
            DB = []
            for i, j in enumerate(A):  # 这一步可以进行二分查找优化
                if j > value or value > B[i]:
                    DA.append(j)
                    DB.append(B[i])
            A = DA.copy()
            B = DB.copy()
            if not A:
                return index + 1
    return -1


def binary_search(nails, start, end, compare_num):
    """
    为每个木板计算可以钉牢该木板的第一个出现的钉子位置
    :param nails: 按照钉子可以钉的位置顺序排列的二位数组
    :param start: 木板的起始点
    :param end: 木板的终点
    :param compare_num: 之前的所有木板需要的最小的钉子数
    :return: 第一次可以被钉子钉牢的钉子的位置
    """
    length = len(nails)
    # 进行二分查找法
    b_s_start = 0
    b_s_end = length - 1
    nailed_position = -1
    search_min = 0
    while b_s_start <= b_s_end:

        b_s_middle = int((b_s_start + b_s_end) / 2)
        number = nails[b_s_middle][1]

        if number < start:  # 钉子位置小于木板起始点
            b_s_start = b_s_middle + 1

        elif number > end:  # 钉子位置大于木板终点
            b_s_end = b_s_middle - 1

        else:  # 可以被钉牢
            nailed_position = nails[b_s_middle][0]  # 钉子序列中的前nailed_position个钉子，可以将这个木板钉牢
            # 但是b_s_middle并不一定是最小的，导致nailed_position也不一定是最小的。b_s_end需要继续减小
            b_s_end = b_s_middle - 1
            search_min = b_s_middle

    if nailed_position == -1:  # 这个木板不能被钉牢
        return -1
    #  下面从最小的可以钉牢该木板的b_s_middle开始，寻找最小的nailed_position数。
    else:
        search_min += 1  # 因为b_s_middle处的钉子的个数值为nailed_position
        while search_min < length:
            if nails[search_min][1] > end:  # 之后的钉子都不可能钉牢该木板
                break
            # 如果可以钉牢，则选择较小的nailed_position，也就是按顺序的钉子的数最小
            nailed_position = min(nailed_position, nails[search_min][0])

            if nailed_position <= compare_num:  # 小于之前木板所需要的钉子数可以钉牢该木板的话，就停止计算即可
                return compare_num

            search_min += 1  # 继续搜索，寻找最小的nailed_position

        return max(nailed_position, compare_num)  # 返回


def solution(A, B, C):
    """
    数组A、B对应元素代表木板，C元素代表可以钉钉子的位置。计算钉牢所有木板需要的最小的钉子数量。
    二分法查找：时间复杂度O((N + M) * log(M))
    :param A: 正整数数组
    :param B: 正整数数组
    :param C: 正整数数组
    :return: 最小的钉子数量
    """
    nails_c = sorted(enumerate(C), key=lambda x: x[1])  # 按照值的大小排列，索引是无序的。索引代表着前几个钉子
    result = -1
    for i in range(len(A)):
        result = binary_search(nails_c, A[i], B[i], result)
        if result == -1:
            return -1
    return result + 1  # 因为索引从0开始，因此需要加1

