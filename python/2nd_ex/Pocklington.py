import random

def make_n(F, num_size):
    R = random.getrandbits(num_size // 2) & ~1
    return R * F + 1

def make_F(F, num_size):
    bit_size = 2 ** (num_size // 2 + 1)
    while F >= bit_size:
        F = (F & 1) + (F >> 1)
    return F
