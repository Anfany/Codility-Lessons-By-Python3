# -*- coding：utf-8 -*-
# &Author  AnFany
# for P91.3 HilbertMaze

"""
利用热力图绘制迷宫，验证创建迷宫的函数是否正确
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as col
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号


def hilbert_maze(n):
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
                up.append(i + i[1:])  # 中间空白只留一个

            # 下半部分
            down = []
            #  左下角的迷宫是小迷宫顺时针旋转90度构成的
            left_down = list(map(list, zip(*maze_list[::-1])))
            #  右下角的迷宫是逆时针旋转90度构成的
            right_down = list(map(list, zip(*maze_list)))[::-1]

            for l, r in zip(left_down, right_down):
                down.append(l + r[1:])  # 中间空白只留一个

            # 上下合并
            merge = up + down[1:]  # 中间空白只留一个

            m += 1
            #  小迷宫相交处添加石块
            merge[2**m][1] = 1
            merge[2**m-1][2**m] = 1
            merge[2**m][2**(m+1)-1] = 1

            maze_list = merge.copy()

        return maze_list


def plot_maze(n):
    """
    绘制N=n的希尔特迷宫
    :param n: 迷宫的大小
    :return: 希尔特迷宫
    """
    maze_list = hilbert_maze(n)
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
    #  设置标题
    ax.set_title('N=%d时的希尔伯特迷宫' % n)
    #  保存迷宫
    plt.savefig(r'C:\Users\GWT9\Desktop\hilbert_%d.jpg' % n)
    #  显示迷宫
    plt.show()
