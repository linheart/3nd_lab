#include "common.h"
#include "miller.h"
#include "Pocklington.h"
#include <iostream>

int main() {
  int num_size;
  cout << "Input bit size: ";
  cin >> num_size;
  vector<int> prime_numbers;
  prime_numbers = sieve(500);

  for (int i = 1; i < 11; i++) {
		int F = gen_prime_num(prime_numbers, num_size / 2 + 1, 1);
		int n = make_n(F, num_size / 2);
    int res = pocklington(F, n, 10);
    if (res == -1)
      cout << n << " sost" << endl;
    else if (res == 0)
      cout << n << " maybe prost" << endl;
    else
      cout << n << " prost" << endl;
  }

  return 0;
}
