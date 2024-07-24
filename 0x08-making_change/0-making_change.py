#!/usr/bin/python3
"""contains the making_change function"""


def makeChange(coins, total):
    """"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    return makeChangeHelper(coins, total)


def makeChangeHelper(coins, current_total):
    """"""
    res, mod = getDividendAndMod(current_total, coins[0])

    if mod == 0:
        return res
    
    # check if this is the last coin
    if mod != 0 and len(coins) == 1:
        return -1
    
    if res == 0:
        return makeChangeHelper(coins[1:], mod)
    
    arr = []
    for x in range(res + 1):
        possible_min = makeChangeHelper(coins[1:], x * coins[0] + mod)
        if possible_min == -1:
            continue
        arr.append(res - x + possible_min)
    return min(arr) if len(arr) > 0 else -1


def getDividendAndMod(quotient, divisor):
    """"""
    return (quotient // divisor, quotient % divisor)
