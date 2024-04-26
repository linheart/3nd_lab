#include "Pocklington.h"
#include "common.h"
#include "gost.h"
#include "miller.h"
#include <iostream>

int main() {
  cout << "1 - Miller's Test" << endl;
  cout << "2 - The Pocklington Test" << endl;
  cout << "3 - The procedure for generating prime numbers GOST R 34.10-94"
       << endl;

  int opt;
  cout << "Select an option: ";
  cin >> opt;

  if (opt > 3 || opt < 1)
    err();

  int num_size;
  cout << "Input bit size: ";
  cin >> num_size;
  if (num_size <= 2)
    err();

  vector<int> prime_numbers = sieve(500);
  int res = 0;
  int n;

  if (opt == 1)
    for (int i = 1; i < 11; i++) {
      while (res != 1) {
        int m = gen_prime_num(prime_numbers, num_size - 1, 1);
        n = 2 * m + 1;
        res = miller_test(n, 10);
      }
			res = 0;
      cout << i << '\t' << n << endl;
    }
	else if (opt == 2)
		for (int i = 1; i < 11; i++) {
			while (res != 1) {
				int F = gen_prime_num(prime_numbers, num_size / 2 + 1, 1);
				n = make_n(F, num_size / 2);
				res = pocklington_test(F, n, 10); 
			}
			res = 0;
			cout << i << '\t' << n << endl;
		}
	else if (opt == 3)
		for (int i = 1; i < 11; i++) {
			int q = gen_prime_num(prime_numbers, num_size / 2, 0);
			cout << i << '\t' << gen_prime(q, num_size) << endl;
		}
  return 0;
}
