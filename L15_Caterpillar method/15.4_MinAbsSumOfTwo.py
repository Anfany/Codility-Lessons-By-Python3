# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 15：Caterpillar method
# P 15.4 MinAbsSumOfTwo


def solution_worse(A):
    """
    返回所有两数和的绝对值的最小值，时间复杂度O(N * N)
    :param A: 数组A
    return: 两数和绝对值的最小值
    """
    length = len(A)
    if length == 1:
        return 2 * abs(A[0])
    A.sort()
    if A[-1] <= 0:
        return min(abs(A[-1] + A[-1]), abs(A[-1] + A[-2]))
    elif A[0] >= 0:
        return min(abs(A[0] + A[0]), abs(A[0] + A[1]))
    else:
        min_num = []
        for i in range(len(A)):
            sum_num = abs(A[i] + A[i])
            for j in range(i+1, len(A)):
                if abs(A[i] + A[j]) > sum_num:
                    break
                else:
                    sum_num = abs(A[i] + A[j])
            min_num.append(sum_num)
        return min(min_num)


def solution(A):
    """
    返回所有两数和的绝对值的最小值，时间复杂度O(N * log(N))
    :param A: 数组A
    return: 两数和绝对值的最小值
    """
    A.sort()
    f_pos = 0
    s_pos = len(A) - 1
    min_num = 2*10**9
    while f_pos <= s_pos:
        min_num = min(min_num, abs(A[f_pos]+A[s_pos]))
        if abs(A[f_pos]) > abs(A[s_pos]):  # 说明f_pos位置一定为负数，此时需要增大负数的值使得和值绝对值变小，因此前一个索引加1
            f_pos += 1
        else:  # f_pos位置的数为一个较小的负数或者正数，因此要减小后面正数的数值，为了获取较小的和值
            s_pos -= 1
        if min_num == 0:  # 因为两数和绝对值最小为0，提前退出
            return 0
    return min_num


