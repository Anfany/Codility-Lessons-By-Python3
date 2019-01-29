# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 9：Maximum slice problem
# P 9.2 MaxProfit


def solution(A):
    """
    返回数组A所代表的股价，可以获得的利润的最大值
    :param A: 股价数组
    :return: 最大利润
    """
    if len(A) == 1:
        return 0
    else:
        profit = [0]  # 最小利润就是0，此处设置是为了编程方便，否则后文需要增加判断非负的条件
        buy, sell = -1, -1
        for i in A:
            if buy == -1:
                buy = i
            else:
                if sell == -1 and i > buy:
                    sell = i
                elif sell != -1 and i > sell:
                    sell = i
                elif i < buy:
                    if sell != -1:
                        profit.append(sell - buy)
                    buy = i
                    sell = -1
        profit.append(sell - buy)
        return max(profit)


