# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 91：Tasks from Indeed Prime 2016 challenge
# P 91.2 TreeProduct


def solution(A, B):
    """
    返回数组A，数组B构成的树的最大树积
    门岗与门岗之间如果有桥直接相连，则只能有一条
    :param A: 数组
    :param B: 数组
    :return: 最大树积
    """
    C = A + B
    count_dict = {}
    for i in C:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    # 只要出现次数大于1的均视为中心
    center = [j for j in count_dict if count_dict[j] > 1]
    length = len(center)  # 中心的个数
    length_a = len(set(C))   # 所有节点的个数
    if length <= 1:  # 只有一个中心或者没有中心的，就不破坏任何桥
        return str(len(A) + 1)
    elif length == 2:  # 如果只有2个中心的，则中心之间肯定有桥
        if length_a == 4:  # 如果每个中心只有一个非中心的连接点，不用断掉桥
            return str(5)
        else:
            product = 1
            for key in center:  # 如果不是每个中心只有一个非中心的连接点，则断开中心之间的桥即可
                product *= count_dict[key]
            return str(product)
    else:
        if length_a == length:  # 环形的
            if length_a <= 4:
                return str(length_a + 1)
            else:
                one = length_a // 2  # 破坏掉2个桥，使得每部分的桥数相同或者为连续的数字
                return str((length_a - one) * one)
        else:
            return str(18)




print(solution([0, 1, 2, 3], [1, 2, 3, 4]))