import random

def brute_force_of_divisors(num):
    if num <= 1:
        return [num]
    i = 2
    q = []
    while num != 1:
        if num % i == 0:
            if i not in q:
                q.append(i)
            num //= i
        else:
            i += 1
    return q


def miller_test(n, t):
    q = brute_force_of_divisors(n - 1)
    a = [random.randint(2, n - 1) for _ in range(t)]
    for i in a:
        res = i % n
        for j in range(2, n):
            res *= i
            res %= n
        if res != 1:
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

def make_m(m, num_size):
    bit_size = 2 ** num_size
    while m >= bit_size:
        m = (m & 1) + (m >> 1)
    return m
