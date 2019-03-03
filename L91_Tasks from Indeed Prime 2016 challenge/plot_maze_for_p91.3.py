# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 91：Tasks from Indeed Prime 2016 challenge
# For P91.3 HilbertMaze

"""
利用热力图绘制迷宫，验证创建迷宫的函数hilbert_maze_array和hilbert_maze_coordinate是否正确
hilbert_maze_array：利用数组的钻旋转得到迷宫数组
hilbert_maze_coordinate：利用坐标的转换得到迷宫数组
最后绘制出起始点到结束点的路径
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as col
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号


#  数组旋转方式建立迷宫数组的函数
def hilbert_maze_array(n):
    """
    根据大小为N=1的迷宫的数组，生成大小为N=n的迷宫的数组
    :param n: 迷宫大小的n
    :return: 返回N=n的迷宫的数组
    """
    #  首先构造n=1时的迷宫
    maze_list = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
    if n == 1:
        return maze_list
    else:
        m = 1
        while m < n:
            #  上半部分是2个一样的
            up = []
            for i in maze_list:
                up.append(i + i[1:])

            #  左下角的迷宫是小迷宫顺时针旋转90度构成的
            left_down = list(map(list, zip(*maze_list[::-1])))
            #  右下角的迷宫是逆时针旋转90度构成的
            right_down = list(map(list, zip(*maze_list)))[::-1]

            down = []
            for l, r in zip(left_down, right_down):
                down.append(l + r[1:])

            # 上下合并
            merge = up + down[1:]

            m += 1
            #  小迷宫相交处添加石块
            merge[2**m][1] = 1
            merge[2**m-1][2**m] = 1
            merge[2**m][2**(m+1)-1] = 1

            maze_list = merge.copy()
        return maze_list


# 坐标转换方式建立迷宫数组的函数
def judge_walkable(n, x, y):
    """
    判断N=n的迷宫中，坐标为(x,y)的网格是否可以走过去，是的话0，否则返回1
    超出迷宫边界的不在此处考虑，在函数point_go中判断
    注意：题目中的迷宫最左上、左下角的网格坐标为(0, 2**(N+1)), (0, 0),本程序中分别定义为(0,0)，(2**(N+1),0)
    因此在寻找路径的时候，会对开始、结束的坐标也进行相应的转换
    :param n: 迷宫的行、列数均为2**(N+1)+1
    :param x: 网格的横坐标
    :param y: 网格的纵坐标
    :return:  判断此网格是否可以走过去，没有岩石说明就可以走过去
    """
    #  需要将坐标(x,y)等价转换到N=1的迷宫中的网格。
    #  此时给出N=1中的坐标的关系
    maze_list = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
    # N=1的迷宫中各个网格的情况
    maze_dict = {(i, j): maze_list[i][j] for i in range(len(maze_list)) for j in range(len(maze_list[i]))}

    while (x, y) not in maze_dict or n != 1:
        # 首先判断处在小迷宫相交地方的三个网格
        if x == 2 ** n:
            if y == 1:   # 左上，左下相交
                return 1
            elif y == 2 ** (n + 1) - 1:  # 右上，右下相交
                return 1
            else:
                return 0
        if y == 2 ** n:
            if x == 2 ** n - 1:   # 左上，右上相交
                return 1
            else:
                return 0

        # 然后判断是否处于四周,
        if x == 0 or x == 2 ** (n+1):
            return 0
        if y == 0 or y == 2 ** (n+1):
            return 0

        #  根据所在不同区域进行不同的变化
        if 1 <= x < 2**n < y < 2**(n+1):  # 右上
            y -= 2**n  # 向左平移2**n

        elif 1 <= y < 2**n < x < 2**(n+1):  # 左下
            #  首先逆时针旋转90度, 原始的a行b列变为2**n-b行a列
            a = x - 2 ** n
            b = y
            x, y = 2 ** n + 2 ** n-b, a
            # 然后向上平移2**n个单位
            x -= 2 ** n
        elif 2**n < x < 2**(n+1)and 2**n < y < 2**(n+1):  # 右下
            #  首先顺时针旋转90度, 原始的a行b列变为b行(2**n-a)列
            a = x - 2 ** n
            b = y - 2 ** n
            x, y = 2 ** n + b, 2**n + 2**n - a
            # 然后向上平移2**n个单位
            x -= 2 ** n
            # 然后向左平移2**n个单位
            y -= 2 ** n
        n -= 1
    return maze_dict[(x, y)]


def hilbert_maze_coordinate(n):
    maze_list = []
    count = 2 ** (n+1) + 1
    for i in range(count):
        maze_list.append([judge_walkable(n, i, j) for j in range(count)])
    return maze_list


#  利用A*获得起始点到结束点的最优路径
def point_go(n, x, y):
    """
    坐标为(x,y)的网格，在迷宫中可以去的坐标集合，上下左右不出迷宫边界，没有石块就可以抵达
    :param n: 表示迷宫的大小
    :param x: 网格的横坐标
    :param y: 网格的纵坐标
    :return: 可以去的坐标的集合
    """
    point_list = []
    length = 2 ** (n+1) + 1
    # 上
    if x >= 1:
        if not judge_walkable(n, x-1, y):
            point_list.append((x - 1, y))
    # 下
    if x < length - 1:
        if not judge_walkable(n, x+1, y):
            point_list.append((x + 1, y))
    # 左
    if y >= 1:
        if not judge_walkable(n, x, y-1):
            point_list.append((x, y - 1))
    # 右
    if y < length - 1:
        if not judge_walkable(n, x, y+1):
            point_list.append((x, y + 1))
    return point_list


def manhattan(a, b, c, d):
    """
    计算坐标为(a,b)的网格与坐标为(c,d)的网格之间的曼哈顿距离
    曼哈顿距离：对应网格的横坐标差的绝对值与纵坐标的差的绝对值之和
    :param a: 开始网格的横坐标
    :param b: 开始网格的纵坐标
    :param c: 结束网格的横坐标
    :param d: 结束网格的纵坐标
    :return: 曼哈顿距离
    a,b = 2, 8
    c,d = 6, 7
    返回 |2-6| +|8-7| = 5
    """
    return abs(a - c) + abs(b - d)


def solution(N, A, B, C, D):
    """
    利用A*算法，返回迷宫中从起始点到结束点的最短路径
    需要注意的是，题目中的网格坐标和数组中的网格坐标是相反的，现在按照数组为准
    因此需要将题目中的起始点，和结束点的坐标进行转换。
    时间复杂度为O(2**(2*N))
    :param N: 定义迷宫大小
    :param A: 起始点的X坐标
    :param B: 起始点的Y坐标
    :param C: 结束点的X坐标
    :param D: 结束点的Y坐标
    :return: 最短路径的步数
    """
    if A == C and B == D:
        return []

    # 真正的起始点、结束点的坐标
    start_a, start_b = 2 ** (N + 1) - B, A
    end_c, end_d = 2 ** (N + 1) - D, C

    # 开始A*算法
    close_list = {}  # 已经走过的网格的集合,
    open_list = {(start_a, start_b): [(start_a, start_b), 0]}   # 将要走的网格的集合
    while (end_c, end_d) not in open_list and open_list and len(open_list):
        #  选择open_list里面代价函数最小的网格
        cost_least = min(open_list.items(), key=lambda k: k[1][1])[0]

        # 计算可以去的相邻的网格
        x, y = cost_least
        point_list = point_go(N, x, y)

        copy_open_list = open_list.copy()
        if point_list:
            for j in point_list:
                if j in close_list:  # 忽略
                    pass
                elif j in open_list:  # 需要对比值，选择较小的，并且更改父亲的节点
                    new_cost = 1 + manhattan(j[0], j[1], end_c, end_d)
                    if new_cost < open_list[j][1]:
                        copy_open_list[j][0] = cost_least
                else:
                    copy_open_list[j] = [(x, y), 1 + manhattan(j[0], j[1], end_c, end_d) + open_list[(x, y)][1]]

        #  存储到已经走过的网格中
        close_list[cost_least] = open_list[cost_least][0]
        del copy_open_list[cost_least]

        open_list = copy_open_list

    if not open_list:  # 无解
        return []
    else:  # 获得最佳的路径
        close_list[(end_c, end_d)] = open_list[(end_c, end_d)][0]
        end_sign = 0
        path_list = [(end_c, end_d)]
        while end_sign != (start_a, start_b):
            end_sign = close_list[path_list[-1]]
            path_list.append(end_sign)
    # 为了使得坐标和迷宫是一样的，现在进行转换，主要是为了验证结果的正确性
    trans_list = []
    for h in path_list:
        trans_list.append([h[1], 2 ** (N+1) - h[0]])
    return path_list[::-1]


# 绘制迷宫的函数以及路径的函数
def plot_maze(n, f, path_list=[]):
    """
    绘制N=n的希尔特迷宫
    :param n: 迷宫的大小
    :param f: 建立迷宫数组的函数
    :param path_list: 存储路径中坐标的列表，如果为空，则不绘制，否则绘制
    :return: 希尔特迷宫
    """
    maze_list = eval(f)(n)
    np_array = np.array([np.array(i) for i in maze_list])
    fig, ax = plt.subplots(figsize=(10, 10))

    # 迷宫的大小
    maze_length = len(maze_list)
    #  设置坐标轴刻度
    ax.set_xticks(np.arange(maze_length))
    ax.set_yticks(np.arange(maze_length))
    #  再次设置坐标轴刻度，为了使得坐标轴标记居于中央
    ax.set_xticks(np.arange(maze_length+1)-0.5, minor=True)
    ax.set_yticks(np.arange(maze_length+1)-0.5, minor=True)
    #  设置坐标轴标签
    label = list(range(maze_length))
    ax.set_xticklabels(label, fontdict={'size': 10})
    ax.set_yticklabels(label[::-1], fontdict={'size': 10})
    #  自定义颜色
    blank_color = 'white'  # 空白的
    stone_color = '#7F7FFF'  # 石块的颜色
    cmap_af = col.LinearSegmentedColormap.from_list('anfany', [blank_color, stone_color])
    ax.imshow(np_array, cmap=cmap_af)
    for edge, spine in ax.spines.items():
        spine.set_visible(False)
    ax.grid(which='minor', color="k", linewidth=1.5)
    # 开始绘制路径和节点
    if path_list:
        x_list = [i[0] for i in path_list]
        y_list = [j[1] for j in path_list]
        #  绘制路径和节点，因为绘图的坐标和正常的坐比是相反的，因此x，y互换
        ax.plot(y_list, x_list, '-o', lw='5', c='r', mfc='r', ms=6)
        #  绘制起点
        ax.scatter([y_list[0]], [x_list[0]], s=99, c='r', label='起点(%d, %d)' %(y_list[0], x_list[0]))
        #  绘制终点
        ax.scatter([y_list[-1]], [x_list[-1]], s=99, c='y', label='终点(%d, %d)' %(y_list[-1], x_list[-1]))
        ax.legend()
        #  设置标题
        ax.set_title('N=%d时的希尔伯特迷宫，最小步数：% d' % (n, len(path_list)-1))
    else:
        if path_list:
            ax.set_title('N=%d时的希尔伯特迷宫，建立迷宫的函数：%s' % (n, f))

    #  保存迷宫
    plt.savefig(r'C:\Users\anaifan\Desktop\hilbert_%d_%s.png' % (n, f))
    #  显示迷宫
    plt.show()


# 最终的函数
if __name__ == "__main__":
    N = 5
    A = 2
    B = 4
    C = 62
    D = 60
    maze_list_array = hilbert_maze_array(N)
    maze_list_coordinate = hilbert_maze_coordinate(N)

    if maze_list_array == maze_list_coordinate:
        best_path = solution(N, A, B, C, D)
        plot_maze(N, 'hilbert_maze_array', best_path)
    else:
        print('两个创建迷宫的函数不一样')
        plot_maze(N, 'hilbert_maze_array', [])
        plot_maze(N, 'hilbert_maze_coordinate', [])


