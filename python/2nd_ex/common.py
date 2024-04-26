import random 

def rem_a(a, n):
    for i in a:
        res = i % n
        for _ in range(2, n):
            res *= i
            res %= n
        if res != 1:
            return -1
    return 0

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

def gen_prime_num(prime_numbers, num_size, flag):
    num = 1
    while True:
        prime_num = random.choice(prime_numbers)
        if flag == 1:
            prime_num **= random.randint(0, num_size - 1)
        num *= prime_num
        if num > 2 ** num_size - 1:
            num = 1
        elif num >= 2 ** (num_size - 1):
            return num
