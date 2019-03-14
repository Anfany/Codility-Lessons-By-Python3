# -*- coding：utf-8 -*-
# &Author  AnFany
# Lesson 92：Tasks from Indeed Prime 2016 College Coders challenge
# P 92.2 SocksLaundering


def solution(K, C, D):
    """
    :param K: 洗衣机一次可以洗的袜子的最大只数
    :param C: 干净袜子
    :param D: 脏袜子
    :return: 可以得到的最大的干净袜子的双数
    """
    # 首先获得干净袜子中的双数
    pair_sock = 0
    sock_dict = {}
    for i in list(set(C)):
        count = C.count(i)
        pairs = count // 2
        pair_sock += pairs
        rest = count % 2
        if rest:
            sock_dict[i] = 1

    # 脏袜子
    sock_dict_dark = {}
    for j in D:
        if j in sock_dict_dark:
            sock_dict_dark[j] += 1
        else:
            sock_dict_dark[j] = 1

    # 开始洗袜子
    if K == 0:
        return pair_sock
    for h in sock_dict:
        if h in sock_dict_dark:
            pair_sock += 1
            sock_dict_dark[h] -= 1
            if sock_dict_dark[h] <= 1:
                del sock_dict_dark[h]
            K -= 1
            if K == 0:
                return pair_sock

    #  计算sock_dict_dark里面的最大双数
    if K < 2 or len(sock_dict_dark) == 0:
        return pair_sock

    for r in sock_dict_dark:
        number = sock_dict_dark[r]
        n = number // 2
        d = min(n, K // 2)
        K -= 2 * d
        pair_sock += d
        if K <= 1:
            break
    return pair_sock

