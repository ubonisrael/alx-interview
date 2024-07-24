#!/usr/bin/python3
"""contains the making_change function"""


def makeChange(coins, total):
    """"""
    coins.sort(reverse=True)
    return makeChangeHelper(coins, total, None)


def makeChangeHelper(coins, current_total, tmp):
    """"""
    res, mod = getDividendAndMod(current_total, coins[0])

    if tmp and res >= tmp:
        return -1

    if mod == 0:
        return res
    
    # check if this is the last coin
    if mod != 0 and len(coins) == 1:
        return -1
    
    if res == 0:
        return makeChangeHelper(coins[1:], mod, tmp)
    
    for x in range(res + 1):
        y = makeChangeHelper(coins[1:], x * coins[0] + mod, tmp)
        if y == -1:
            continue
        possible_min = res - x + y
        tmp = tmp if tmp and tmp < possible_min else possible_min
    return tmp if tmp else -1


def getDividendAndMod(quotient, divisor):
    """"""
    return (quotient // divisor, quotient % divisor)
