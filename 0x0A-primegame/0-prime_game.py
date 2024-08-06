#!/usr/bin/python3
"""contains the isWinner function"""


def isWinner(x, nums):
    """calculates the winner after x rounds with nums array"""
    # initialize win count
    ben = 0
    maria = 0
    rounds = x

    for n in nums:
        if rounds == 0:
            break
        rounds -= 1
        if n < 1:
            continue
        if n == 1:
            # ben wins the round automatically
            ben += 1
            continue
        array = list(range(1, n + 1))
        count = 0
        while len(array) > 1:
            prime = array[1]
            count += 1
            new_array = list(filter(lambda x: x % prime != 0, array))
            array = new_array[:]
        if count % 2 == 0:
            ben += 1
        else:
            maria += 1
    
    return None if ben == maria else ("Ben" if ben > maria else "Maria")
