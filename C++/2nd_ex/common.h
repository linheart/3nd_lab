#ifndef COMMON_H // COMMON_H
#define COMMON_H

#include <vector>
#include <cmath>
#include <algorithm>
#include <vector>
#include <random>

using namespace std;

int rem_a(vector<int> a, int n);
vector<int> sieve(int num);
int gen_prime_num(vector<int> prime_numbers, int num_size, int flag);
int gen_rand_num(int start, int end);
vector<int> brute_force_of_divisors(int m);

#endif // COMMON_H
