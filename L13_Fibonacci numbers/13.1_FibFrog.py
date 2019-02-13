# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 13：Fibonacci numbers
# P 13.1 FibFrog


def fib(n=100000):
    """
    构造不大于100000的斐波那契数的列表
    :param n: 最大值
    :return: 斐波那契数列
    """
    fib_list = [1]
    a = fib_list[0]
    b = 1
    while b <= n:
        fib_list.append(b)
        a, b = b, a+b
    return fib_list


def solution(A):
    """
    判断能否按照斐波那契步数过河。先找到过河的跳跃步数，如果相邻的步数是斐波那契数列中相邻的，则可以合并。
    :param A: 表示河面上树叶情况的数组
    :return: 能，返回最好次数。不能，返回-1
    """
    fib_list = fib()
    length = len(A) + 1
    if length in fib_list:  # 一次就可从位置-1跳到位置N
        return 1
    else:
        leaf_fib = []  # 含有树叶的位置
        for index, value in enumerate(A):
            if value == 1:
                leaf_fib.append(index + 1)
        if not leaf_fib:  # 河面没有树叶
            return -1
        else:
            sign = 0  # 判断是否可以完成过河
            for i in leaf_fib:
                forward = step_list[-1]
                if i in fib_list:
                    if leaf_fib[-1] - i in fib_list or leaf_fib[-1] - i == 0:
                        sign = 1
                    else:
                        if i - forward in fib_list:
                            step_list.append(i)
                            if leaf_fib[-1] - i in fib_list:
                                sign = 1
            if sign == 1:
                return len(step_list) - 1
            else:
                return -1



print(solution([0,0,0,1,1,0,1,0,0,0,0]))


