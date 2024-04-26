#include "common.h"

int miller_test(int n, int t) {
  vector<int> q = brute_force_of_divisors(n - 1);
  vector<int> a = {};
  int res = 0;
  int deg = 0;

  for (size_t i = 0; i < t; i++)
    a.push_back(gen_rand_num(2, n - 1));

  if (rem_a(a, n) == -1)
    return -1;

  for (auto i : q) {
    res = 1;
    for (auto j : a) {
      res = j % n;
      deg = (n - 1) / i;
      for (int i = 0; i < deg; i++)
        res = res * j % n;

      if (res != 1)
        break;
    }

    if (res == 1)
      return 0;
  }
  return 1;
}
