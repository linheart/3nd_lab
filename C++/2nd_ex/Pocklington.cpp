#include "common.h"

int pocklington_test(int F, int n, int t) {
  vector<int> q = brute_force_of_divisors(F);
  vector<int> a = {};
  int res;
  int deg;

  for (int i = 0; i < t; i++)
    a.push_back(gen_rand_num(2, n - 1));

  if (rem_a(a, n) == -1)
    return -1;

  for (auto i : a) {
    res = i % n;
    for (auto j : q) {
      deg = (n - 1) / j;
      for (int k = 2; k <= deg; k++)
        res = res * i % n;
      if (res == 1)
        break;
    }
    if (res != 1)
      return 1;
  }
  return 0;
}

int make_n(int F, int num_size) {
  int R = gen_rand_num(pow(2, num_size - 1), pow(2, num_size) - 1);
  R -= R & 1;
  return R * F + 1;
}
