import random
from common import brute_force_of_divisors, rem_a

def pocklington_test(F, n, t):
    q = brute_force_of_divisors(F)
    a = [random.randint(2, n - 1) for _ in range(t)]
    if rem_a(a, n) == -1:
            return -1
    for i in a:
        res = i % n
        for j in q:
            deg = (n - 1) / j
            for _ in range(2, int(deg) + 1):
                res *= i
                res %= n
            if res == 1:
                break
        if res != 1:
            return 1
    return 0


def make_n(F, num_size):
    R = random.getrandbits(num_size // 2) 
    R |= 1 << (num_size // 2 - 1)
    R -= R & 1
    return R * F + 1
