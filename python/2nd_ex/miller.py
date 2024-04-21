import random
from common import brute_force_of_divisors, rem_a

def miller_test(n, t):
    q = brute_force_of_divisors(n - 1)
    a = [random.randint(2, n - 1) for _ in range(t)]

    if rem_a(a, n) == -1:
            return -1

    for i in q:
        res = 1
        for j in a:
            res = j % n 
            deg = (n - 1) / i
            for _ in range(2, int(deg) + 1):
                res *= j
                res %= n
            if res != 1:
                break
        if res == 1:
            return 0
    return 1

def make_n(m):
    return 2 * m + 1
