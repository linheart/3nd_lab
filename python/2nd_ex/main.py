import miller
import Pocklington
import random

# Sieve of Eratosthenes
def sieve(num):
    nums = [i for i in range(2, num + 1)]
    i = 2
    max_num = nums[-1]
    while i ** 2 < max_num:
        if i in nums:
            for j in range(i ** 2 - 2, len(nums), i):
                nums[j] = 0
        i += 1
    return list(filter(lambda x: x != 0, nums))

def gen_prime_num(prime_numbers, num_size):
    num = 1
    bit_size = 2 ** num_size
    while num < bit_size:
        num *= random.choice(prime_numbers) ** random.randint(0, num_size - 1)
    return num


if __name__ == "__main__":
    num_size = int(input())
    if num_size < 2:
        raise Exception("Invalid input")

    res = 0
    prime_numbers = sieve(500)
    F = gen_prime_num(prime_numbers, num_size)
    F = Pocklington.make_F(F, num_size)
    n = Pocklington.make_n(F, num_size)
    # arr = [437, 657, 779, 1189, 1191, 1533, 1785, 2071, 2327, 2249, 2249, 3379, 3701, 4009, 4647, 5007, 5211, 8891, 9451, 9837, 9943, 6141, 6259, 6951, 7157, 7483]
    # for _ in range(100):
    #     for i in arr:
    #         res = miller.miller_test(i, 10)
    #         if res != -1 and res != 0:
    #             print(i, res)
    #             raise Exception("wrong")
    # for _ in range(10):
    #     while res != 1:
    #         m = miller.make_m(prime_numbers, num_size)
    #         n = miller.make_n(m)
    #         res = miller.miller_test(n, 10)
    #         if res == 1:
    #             print(n)
    #     res = 0
    #     # if res == -1:
    #     #     print(f"{n} - составное число")
    #     # elif res == 0:
    #     #     print(f"вероятно, {n} - составное число")
    #     # else:
    #     #     print(f"{n} - простое число")
