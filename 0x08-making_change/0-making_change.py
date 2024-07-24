#!/usr/bin/python3
"""contains the making_change function"""


# def makeChange(coins, total):
#     """"""
#     if total <= 0:
#         return 0
#     coins.sort(reverse=True)
#     return makeChangeHelper(coins, total)


# def makeChangeHelper(coins, current_total):
#     """"""
#     res, mod = getDividendAndMod(current_total, coins[0])

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


# def getDividendAndMod(quotient, divisor):
#     """"""
#     return (quotient // divisor, quotient % divisor)


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
