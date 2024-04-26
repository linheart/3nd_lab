#include "common.h"
#include <iostream>

int make_N(int q, int num_size) {
  int eps = gen_rand_num(0, 1);
  int N = (pow(2, (num_size - 1)) / q) + (pow(2, num_size - 1) * eps / q);
  return N + (N & 1);
}

int gen_prime(int q, int num_size) {
  while (1) {
    int N = make_N(q, num_size);
    int u = 0;
    while (1) {
      int p = (N + u) * q + 1;

      if (p > pow(2, num_size))
        break;

      int res = 2 % p;

      for (int i = 2; i < p; res = res * 2 % p, i++)
        ;

      if (res == 1) {
        res = 2 % p;

        for (int i = 2; i <= N + u; res = res * 2 % p, i++)
          ;

        if (res != 1)
          return p;
      }
      u += 2;
    }
  }
}
