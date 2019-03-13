# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 99：Future training
# P 99.5 PolygonConcavityIndex


def solution(A):
    """
    判断A中点组成的多边形是否是凸多边形，是的话返回-1，不是的话返回在凸包内部的任意一点的索引
    利用Graham扫描算法得到凸包
    :param A: 顶点的坐标
    :return: -1或者凸包内部任意点的索引
    """
    if len(A) == 3:
        return -1
    # 所有点的集合
    point_set = []
    for i in range(len(A)):
        point_set.append([i, [A[i].x, A[i].y]])  # 题目中设定的数据结构
        # point_set.append([i, [A[i][0], A[i][1]]])
    # 选出所有点中纵坐标最小的点，纵坐标相同的选择横坐标最小的点
    point_set.sort(key=lambda s: [s[1][1], s[1][0]])
    min_y_point = point_set[0]  # 参考点P0
    # 将上面选择的点，转移到原点，计算其他所有点转移后和原点构成的向量和x轴正向的夹角
    # 按照夹角从小到大排列，相同角度的, 按照y的降序排列
    more_than_zero = []  # 大于0的升序排列，相同值的按照y的降序排列
    less_than_zero = []  # 小于0的升序排列，相同值的按照y的降序排列
    zero = []   # 等于0的按照y值的降序排列
    for p in point_set[1:]:
        point = [p[1][0] - min_y_point[1][0], p[1][1] - min_y_point[1][1]]
        if point[0] != 0:
            tan = point[1] / point[0]
            if tan >= 0:
                more_than_zero.append([p[0], [tan, point[1]], point])
            else:
                less_than_zero.append([p[0], [tan, point[1]], point])
        else:
            zero.append([p[0], [0, point[1]], point])

    more_than_zero.sort(key=lambda m: [m[1][0], -m[1][1]])
    less_than_zero.sort(key=lambda m: [m[1][0], -m[1][1]])
    zero.sort(key=lambda m: -m[1][1])

    # 合并后，所有点是按着夹角逆时针排列的
    trans_point_angle = more_than_zero + zero + less_than_zero

    #  开始位置添加第一个点P0
    trans_point_angle.insert(0, [point_set[0][0], [0, 0], [0, 0]])
    #  结尾位置添加第一个点P0
    trans_point_angle.append(trans_point_angle[0])

    # 把前2个点p0, p1放入栈中，把p1后面的点p2作为评判点，如果向量的叉积V_p0p2*V_p0p1<0,说明p2在p0p1的逆时针方向，是对的，如果为0，
    # 说明三点共线;如果大于0，说明p2在p0p1的顺时针方向，说明P1点是凹进去的
    current = [trans_point_angle[0], trans_point_angle[1]]
    for index in trans_point_angle[2:]:
        p0, p1, p2 = [current[0], current[1], index]
        p0_p = p0[2]
        p1_p = p1[2]
        p2_p = p2[2]
        p0p2 = p2_p[0] - p0_p[0], p2_p[1] - p0_p[1]
        p0p1 = p1_p[0] - p0_p[0], p1_p[1] - p0_p[1]
        product = p0p2[0] * p0p1[1] - p0p2[1] * p0p1[0]

        if product < 0:
            current = [current[1], index]
        elif product == 0:
            current = [current[0], index]
        else:
            return current[1][0]
    return -1


