# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 92：Tasks from Indeed Prime 2016 College Coders challenge
# P 92.1 TennisTournament


def solution(P, C):
    """
    给定选手数P，球场数C，返回同时进行比赛的场数
    :param P: 选手数
    :param C: 球场数
    :return: 比赛场数
    """
    return min(C, P // 2)