# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 90：Tasks from Indeed Prime 2015 challenge
# P 90.1 LongestPassword


def solution(S):
    """
    返回字符串S中符合条件的最长的字符串长度
    :param S: 字符串
    :return: 最长字符串的长度
    """
    split_list = S.split(' ')
    print(split_list)

    lower = list(range(ord('a'), ord('z')+1))
    upper = list(range(ord('A'), ord('Z')+1))
    digit = list(range(ord('0'), ord('9')+1))

    str_length = []
    for i in split_list:
        sign = 1
        alpha = 0
        number = 0
        for h in i:
            if ord(h) in lower or ord(h) in upper:
                alpha += 1
            elif ord(h) in digit:
                number += 1
            else:
                sign = 0
                break
        if sign:
            if not alpha % 2 and number % 2:
                str_length.append(len(i))
    if len(str_length) == 0:
        return -1
    else:
        return max(str_length)



