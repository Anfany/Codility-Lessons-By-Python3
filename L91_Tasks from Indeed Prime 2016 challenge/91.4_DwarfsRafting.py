# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 91：Tasks from Indeed Prime 2016 challenge
# P 91.4 DwarfsRafting


def encode_str(seat_str, n):
    """
    根据座位字符串，返回座位行数为键，座位列号为值的字典
    :param seat_str: 存放座位信息的字符串
    :param n: 木筏上座位的行数和列数
    :return: 字典
    """
    # 将木筏分为左上，右上，左下，右下四部分，这四部分分别定义为0， 1， 2， 3
    seat_dict = {i: 0 for i in range(4)}
    if not seat_str:  # 字符串为空
        return seat_dict
    else:
        seat_dict = {i: 0 for i in range(4)}
        str_list = seat_str.split(' ')  # 间隔一个空格
        for i in str_list:
            if len(i) == 2:  # 行号可能是2位数
                row, column = i
            else:
                row, column = i[:2], i[2]
            if int(row) <= n / 2:  # 是上半部分的
                if ord(column) - ord('A') < n / 2:  # 左上
                    seat_dict[0] += 1
                else:  # 右上
                    seat_dict[1] += 1
            else:  # 是下半部分的
                if ord(column) - ord('A') < n / 2:  # 左下
                    seat_dict[2] += 1
                else:  # 右下
                    seat_dict[3] += 1
    return seat_dict


def solution(N, S, T):
    """
    根据已经站的座位，使得木筏各个部分保持平衡的前提下可以容纳的最多人数
    :param N: 偶数，代表座位的行数和列数
    :param S: 承载木桶的座位
    :param T: 承载其他矮人的座位
    :return:  新容纳矮人的最大人数
    """
    barrels_dict = encode_str(S, N)  # 木桶占据的座位
    pepole_dict = encode_str(T, N)   # 矮人们已经占据的座位

    # 每个部分的座位总数为
    all_seats = (N // 2) ** 2

    # 计算每个部分已有矮人的数量和剩余空位的数量确定容纳的人数
    part_dict = {k: [pepole_dict[k], all_seats-pepole_dict[k]-barrels_dict[k]] for k in pepole_dict}

    #  左上和右下部分
    sum_left_up = sum(part_dict[0])
    sum_right_down = sum(part_dict[3])
    #  当一部分的已有矮人的数量和剩余空位的数量之和不小于另一部分的已有矮人的数量，才可以平衡
    if sum_left_up >= part_dict[3][0] and sum_right_down >= part_dict[0][0]:
        left_up_right_down = min(sum_left_up, sum_right_down)  # 左上和右下部分每一部分最多可以承载的人数
    #  计算左上和右下部分，每一部分可以新承载矮人的数
        new_left_up_right_down = 2 * left_up_right_down - part_dict[0][0] - part_dict[3][0]
    else:
        return -1

    #  左下和右上部分
    sum_left_down = sum(part_dict[2])
    sum_right_up = sum(part_dict[1])
    #  当一部分的已有矮人的数量和剩余空位的数量之和不小于另一部分的已有矮人的数量，才可以平衡
    if sum_left_down >= part_dict[1][0] and sum_right_up >= part_dict[2][0]:
        left_down_right_up = min(sum_left_down, sum_right_up)  # 左下和右上部分每一部分最多可以承载的人数
    #  计算左下和右上部分，每一部分可以新承载矮人的数
        new_left_down_right_up = 2 * left_down_right_up - part_dict[1][0] - part_dict[2][0]
    else:
        return -1

    return new_left_up_right_down + new_left_down_right_up






