import miller
from bf_of_div import brute_force_of_divisors

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

if __name__ == "__main__":
    prime_numbers = sieve(500)
    num_size = int(input())
    if num_size < 2:
        raise Exception("Invalid input")
    m = miller.make_m(prime_numbers, num_size)
    n = miller.make_n(m)
    for i in range(100):
        print(miller.miller_test(prime_numbers, n, 10))
