# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 92：Tasks from Indeed Prime 2016 College Coders challenge
# P 92.3 ArrayRecovery


def computer_factorial(n, m):
    """
    计算可能性
    :param n: 可选范围内数字的个数
    :param m: 都是这个可选范围的长度
    :return: 阶乘的比值(n - 1 + m)!/(m! * (n-1)!)模(10 ** 9 +7)
    """
    min_num = min(n - 1, m)
    max_num = max(n - 1, m)
    fenzi = list(range(max_num + 1, max_num + min_num + 1))
    fenmu = list(range(1, min_num + 1))

    # 计算一个数可以分解为质因数的字典
    def decompose(num):
        """
        将数num分解为以素因素为键，含有该素因素的个数为值的字典
        :param num: 正整数
        :return: 字典
        例如num：300，返回{2:2,3:1,5:2}
        """
        prime = {}
        count_2 = 0
        #  首先把偶数去除掉
        while num % 2 == 0:
            count_2 += 1
            num /= 2
            prime[2] = count_2

        for i in range(3, int(num ** 0.5) + 2, 2):
            count = 0
            while num != 1 and i <= num:
                if num % i == 0:
                    num /= i
                    count += 1
                    prime[i] = count
                else:
                    break
        if int(num) != 1:
            prime[int(num)] = 1
        return prime

    def get_dict(ex_list):
        """
        将数组中的所有数的素因素字典结合在一起
        :param ex_list: 数组
        :return: 结合的字典
        """
        all_dict = {}
        for hh in ex_list:
            son_dict = decompose(hh)
            for j in son_dict:
                if j in all_dict:
                    all_dict[j] += son_dict[j]
                else:
                    all_dict[j] = son_dict[j]
        return all_dict

    zong_dict = get_dict(fenzi)
    fen_dict = get_dict(fenmu)

    for kk in fen_dict:
        zong_dict[kk] -= fen_dict[kk]

    times = 1
    for hu in zong_dict:
        times *= (hu ** zong_dict[hu]) % (10 ** 9 + 7)
    return times % (10 ** 9 + 7)


def solution(B, M):
    """
    返回可以转变为数组B的可能数组的个数
    :param B: 需要还原的数组
    :param M: 元素的最大值
    :return: 可能的个数
    """
    if list(set(B)) == [0]:  # B中元素全为0
        return computer_factorial(M, len(B)) % (10 ** 9 + 7)

    if len(B) == len(set(B)):  # 也就是B中不存在重复的元素，此时A=B[1:] + [大于B[-1]并且不大于M的数]
        return (M - B[-1]) % (10 ** 9 + 7)

    # 此时需要考虑多种情况
    times = 1  # 总的可能性个数
    number_index = {}  # 存储每个值出现的索引，便于计算区间值
    rule_dict = {}  # 存储可能性规则的字典
    index_sign = -1  # 索引限制，对于连续出现的某个数字，只遍历第一个位置的索引，后面的跳过即可
    B = [-1] + B + [-1]  # 为了程序判断，需要在B的前后各加一个小于0的元素
    #  开始多种情况的判断
    for s in range(1, len(B) - 1):  # 开始和结束的元素不考虑
        if s >= index_sign:

            # 开始获得B[s]连续出现的个数
            n = s
            while B[s] == B[n]:
                n += 1

            # 开始分情况讨论
            if B[s] > B[s - 1]:  # 大于前一个数字
                if B[n] > B[s]:  # 小于下一个数字
                    # 此时这些位置的最小值不小于B[n]，并且位置的最后一个肯定是B[n],因此长度减去1
                    rule_dict[s] = [M - B[n] + 1, n - s - 1]
                else:
                    # 此时和后面的数字没关系B[n]，因为后面的数字在之前肯定出现过
                    rule_dict[s] = [M - B[s], n - s]

            else:  # 说明值为B[s]的数字，以前出现过
                #  如果这些位置上的数字为0
                if B[s] == 0:
                    #  获取该位置之前的所有大于0的值中的最小值
                    max_num = B[n]
                    for j in sorted(B[: s]):
                        if j != B[s] and j > B[s]:
                            max_num = j
                            break
                    if B[n] > B[s]:
                        # 此时这些位置的值需要在max_num和B[n]之间，但是可以等于B[n]，并且位置的最后一定为B[n]，长度减去1
                        rule_dict[s] = [max_num - B[n] + 1, n - s - 1]  # fhg
                    else:
                        # 如果0元素一直到最后，此时这些位置的值从1到max_num
                        rule_dict[s] = [max_num - B[s], n - s]  # fhg
                else:
                    # 如果这些位置的数字不为0，因为以前出现过，因此这些位置的最大值不能大于这个数字出现后的数字序列的最小值。
                    # 获取最小值
                    max_num = B[n]
                    for j in sorted(B[number_index[B[s]] + 1: s]):
                        if j != B[s] and j > B[s]:
                            max_num = j
                            break
                    if B[n] > B[s]:
                        #  此时这些位置的最小值不小于B[n]，并且位置的最后一个肯定是B[n],因此长度减去1
                        rule_dict[s] = [max_num - B[n] + 1, n - s - 1]
                    else:
                        # 此时和后面的数字没关系B[n]，因为后面的数字在之前肯定出现过
                        rule_dict[s] = [max_num - B[s], n - s]
            number_index[B[s]] = s
            index_sign = n

    # 开始计算最后的可能性
    for rule in rule_dict:
        count_number, length_rule = rule_dict[rule]
        times *= computer_factorial(count_number, length_rule)
        times = times % (10 ** 9 + 7)
    return times
