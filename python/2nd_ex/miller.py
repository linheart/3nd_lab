import random

def make_m(prime_numbers, num_size):
    m = 1
    bit_size = 2 ** num_size
    while m < bit_size:
        m *= random.choice(prime_numbers) ** random.randint(0, num_size - 1)

    while m >= bit_size:
        m = (m & 1) + (m >> 1)

    return m
