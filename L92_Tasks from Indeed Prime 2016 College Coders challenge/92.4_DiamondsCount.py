# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 92：Tasks from Indeed Prime 2016 College Coders challenge
# P 92.4 DiamondsCount


def solution(X, Y):
    """
    给出平面上的点，得出满足条件的不同菱形的个数
    :param X: 点的横坐标
    :param Y: 点的纵坐标
    :return: 不同菱形的个数
    """
    x_dict = {}  # 横坐标为键，纵坐标为值的字典
    y_dict = {}  # 纵坐标为键，横坐标为值的字典

    for x, y in zip(X, Y):
        if x in x_dict:
            x_dict[x].append(y)
        else:
            x_dict[x] = [y]

        if y in y_dict:
            y_dict[y].append(x)
        else:
            y_dict[y] = [x]
    #  不同的x或者y都必须大于2个，才可能组成满足条件的菱形
    if len(x_dict) <= 2 or len(y_dict) <= 2:
        return 0

    #  开始判断是否可以构成菱形
    count = 0
    for i in x_dict:  # 遍历横坐标
        point_count = x_dict[i]  # 这个横坐标上的点最少为2个，才可能构建菱形
        if len(point_count) >= 2:
            for o in range(len(point_count) - 1):
                for t in range(o + 1, len(point_count)):
                    y_sum = point_count[o] + point_count[t]  # 开始计算纵坐标的均值，需要为整数
                    if y_sum % 2 == 0:
                        y_value = y_sum // 2
                        if y_value in y_dict:  # 纵坐标存在
                            y_point = y_dict[y_value]  # 该纵坐标对应的横坐标序列
                            if len(y_point) >= 2:  # 这个纵坐标上的点也最少也为2个
                                sort_y_point = sorted(y_point)
                                min_num = sort_y_point[0]
                                max_num = sort_y_point[-1]
                                if min_num < i < max_num:  # 横坐标i因为是均值，因此需要在这个序列的最大最小值之间
                                    for j in sort_y_point:
                                        if j < i:
                                            if 2 * i - j in sort_y_point:  # 纵坐标对应的2个横坐标的均值恰好为i
                                                count += 1
                                        else:  # 因为sort_y_point是升序的，一旦大于i，后面的就不可能了
                                            break
    return count



