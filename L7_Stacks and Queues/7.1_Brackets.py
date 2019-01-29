# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 7：Stacks and Queues
# P 7.1 Brackets


def solution(S):
    """
    判断字符串S中的符号是否为正确的嵌套
    :param S: 字符串
    :return: 判断是否为正确的嵌套
    """
    left = '([{'
    brackers_dict = {'(': ')', '[': ']', '{': '}'}
    brackers = []
    if len(S) == 0:
        return 1
    else:
        for i in S:
            if i in left:
                brackers.append(i)
            else:
                try:
                    if brackers_dict[brackers[-1]] == i:
                        brackers.pop(-1)
                    else:
                        return 0
                except IndexError:
                    return 0
        if len(brackers) == 0:
            return 1
        else:
            return 0