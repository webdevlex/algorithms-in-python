def primeNaive(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


import math


def primeSlightlyBetter(n):
    if n < 2:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True


import math


def sieveOfEratosthenes(max):
    flags = [True] * (max + 1)
    flags[0] = flags[1] = False

    prime = 2
    while prime <= int(math.sqrt(max)):
        cross_off(flags, prime)
        prime = get_next_prime(flags, prime)

    return flags


def cross_off(flags, prime):
    for i in range(prime * prime, len(flags), prime):
        flags[i] = False


def get_next_prime(flags, prime):
    next_prime = prime + 1
    while next_prime < len(flags) and not flags[next_prime]:
        next_prime += 1
    return next_prime
