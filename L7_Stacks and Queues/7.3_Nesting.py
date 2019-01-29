# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 7：Stacks and Queues
# P 7.3 Nesting


def solution(S):
    """
    判断字符串是否为正确的嵌套
    :param S: 字符串
    :return: 是正确的返回1，否则返回0
    """
    left_list = []
    for i in S:
        if i == '(':
            left_list.append(0)
        else:
            if len(left_list) == 0:
                return 0
            else:
                left_list.pop(0)
    if len(left_list) != 0:
        return 0
    else:
        return 1