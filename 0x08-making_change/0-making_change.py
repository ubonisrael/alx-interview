#!/usr/bin/python3
"""contains the making_change function"""
# import sys
# sys.setrecursionlimit(10**6)


# # initial solution, the correct one but slow
# def makeChange(coins, total):
#     """"""
#     if total <= 0:
#         return 0
#     coins.sort(reverse=True)
#     return makeChangeHelper(coins, total)


# def makeChangeHelper(coins, current_total):
#     """helper function for makeChange"""
#     res, mod = getQuotientAndMod(current_total, coins[0])

#     if mod == 0:
#         return res

#     # check if this is the last coin
#     if mod != 0 and len(coins) == 1:
#         return -1

#     if res == 0:
#         return makeChangeHelper(coins[1:], mod)

#     arr = []
#     for x in range(res + 1):
#         possible_min = makeChangeHelper(coins[1:], x * coins[0] + mod)
#         if possible_min == -1:
#             continue
#         arr.append(res - x + possible_min)
#     return min(arr) if len(arr) > 0 else -1


def getQuotientAndMod(dividend, divisor):
    """returns the quotient and modulus of a division operation"""
    return (dividend // divisor, dividend % divisor)


# fast solution but inaccurate
def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    count = 0
    if total <= 0:
        return count
    coins.sort(reverse=True)
    index = 0
    coins_length = len(coins)
    remainder = total
    while remainder > 0:
        if index >= coins_length:
            return -1
        res, remainder = getQuotientAndMod(remainder, coins[index])
        count += res
        if remainder == 0:
            break
        index += 1
    return count
