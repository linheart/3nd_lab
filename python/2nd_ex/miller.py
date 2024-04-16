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


def miller_test(prime_numbers, n, t):
    q = brute_force_of_divisors(n - 1)
    a = [random.randint(2, n - 1) for _ in range(t)]
    res = 1
    for i in a:
        if (i ** (n - 1)) % n != 1:
            return -1
    for i in q:
        for j in a:
            res *= j ** ((n - 1) / i) % n 
            if res != 1:
                break
        if res != 1:
            break

    if res == 1:
        return 0
    return 1

def make_n(m):
    return 2 * m + 1

def make_m(prime_numbers, num_size):
    m = 1
    bit_size = 2 ** num_size
    while m < bit_size:
        m *= random.choice(prime_numbers) ** random.randint(0, num_size - 1)

    while m >= bit_size:
        m = (m & 1) + (m >> 1)

    return m
