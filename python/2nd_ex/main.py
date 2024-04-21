import miller
import Pocklington
import gost
from common import sieve, gen_prime_num

if __name__ == "__main__":
    print("1 - Miller's Test")
    print("2 - The Pocklington Test")
    print("3 - The procedure for generating prime numbers GOST R 34.10-94")

    opt = int(input("Select an option: "))
    if opt > 3 or opt < 1:
        raise Exception("Invalid input")
    num_size = int(input("Input bit size: "))
    if num_size < 2:
        raise Exception("Invalid input")

    prime_numbers = sieve(500)
    n = 1

    if opt == 1:
        for i in range(1, 11):
            res = 0
            while res != 1:
                m = gen_prime_num(prime_numbers, num_size - 1, 1)
                n = miller.make_n(m)
                res = miller.miller_test(n, 10)
            print(f"{i}\t", n)

    elif opt == 2:
        for i in range(1, 11):
            res = 0
            while res != 1:
                F = gen_prime_num(prime_numbers, num_size // 2 + 1, 1)
                n = Pocklington.make_n(F, num_size)
                res = Pocklington.pocklington_test(F, n, 10)
            print(f"{i}\t", n)

    elif opt == 3:
        for i in range(1, 11):
            q = gen_prime_num(prime_numbers, num_size // 2, 0)
            print(f"{i}\t", gost.gen_prime(q, num_size))
