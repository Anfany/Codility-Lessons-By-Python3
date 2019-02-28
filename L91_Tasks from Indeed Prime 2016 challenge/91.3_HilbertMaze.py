# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 91：Tasks from Indeed Prime 2016 challenge
# P 91.3 HilbertMaze


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

def solution(N, A, B, C, D):
    """
    在迷宫中，返回从起始点到结束点的最短路径的步数
    :param N: 定义迷宫大小
    :param A: 起始点的X坐标
    :param B: 起始点的Y坐标
    :param C: 结束点的X坐标
    :param D: 结束点的Y坐标
    :return: 最短路径的步数
    """
    hilbert_maze_list = hilbert_maze(N)

