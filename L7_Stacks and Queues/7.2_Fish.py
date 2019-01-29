# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 7：Stacks and Queues
# P 7.2 Fish


def solution(A, B):
    """
    相遇的鱼大鱼吃小鱼
    :param A: A表示鱼的大小
    :param B: 表示鱼游的方向
    :return: 活鱼的数目
    """
    alive_fish = 0
    fish_down = []  # 存储向下游的鱼
    for index, value in enumerate(B):
        if value == 0:
            if len(fish_down) == 0:
                alive_fish += 1
            else:
                #  开始判断吃鱼
                try:
                    while fish_down[-1] < A[index]:
                        fish_down.pop(-1)
                except IndexError:
                    alive_fish += 1
        else:
            fish_down.append(A[index])
    return alive_fish + len(fish_down)
