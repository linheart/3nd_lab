import random

def make_N(q, num_size):
    eps = random.randint(0, 1)
    N = (2 ** (num_size - 1) // q) + (2 ** (num_size - 1) * eps // q)
    return N + (N & 1)

def gen_prime(q, num_size):
    while True:
        N = make_N(q, num_size)
        u = 0
        while True:
            p = (N + u) * q + 1

            if p > 2 ** num_size:
                break
            res = 2 % p

            for _ in range(2, p):
                res = res * 2 % p
            
            if res == 1:
                res = 2 % p
                for _ in range(2, N + u + 1):
                    res = res * 2 % p

                if res != 1:
                    return p
            u += 2



