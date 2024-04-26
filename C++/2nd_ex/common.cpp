#include "common.h"

void err() {
  cerr << "Invalid input" << endl;
  exit(EXIT_FAILURE);
}

int rem_a(vector<int> a, int n) {
  int res = 0;

  for (auto i : a) {
    res = i % n;

    for (int j = 2; j < n; j++) {
      res *= i;
      res %= n;
    }

    if (res != 1)
      return -1;
  }

  return 0;
}

vector<int> brute_force_of_divisors(int num) {
  int i = 2;
  vector<int> q = {};

  if (num <= 1)
    return (vector<int>)num;

  while (num != 1)
    if (num % i == 0) {
      if (find(q.begin(), q.end(), i) == q.end())
        q.push_back(i);
      num /= i;
    } else
      i++;
  return q;
}

int gen_rand_num(int start, int end) {
  random_device rd;
  mt19937 gen(rd());
  uniform_int_distribution<> dis(start, end);
  return dis(gen);
}

int gen_prime_num(vector<int> prime_numbers, int num_size, int flag) {
  int num = 1;
  int prime_num;
  int up_bound = pow(2, num_size) - 1;
  int low_bound = pow(2, num_size - 1);

  while (1) {
    prime_num = prime_numbers[gen_rand_num(0, prime_numbers.size() - 1)];

    if (flag) {
      int max_exp = 1;
      int tmp = prime_num;
      for (; pow(prime_num, max_exp) <= up_bound || max_exp < 2; max_exp++)
        ;
      num *= pow(prime_num, gen_rand_num(1, max_exp - 1));
    } else
      num = prime_num;

    if (num >= low_bound && num <= up_bound)
      return num;
    else if (num >= up_bound)
      num = 1;
  }
}

vector<int> sieve(int num) {
  vector<int> nums;

  for (int i = 2; i <= num; i++)
    nums.push_back(i);

  int max_num = nums.back();

  for (int i = 2; pow(i, 2) < max_num; i++)
    if (find(nums.begin(), nums.end(), i) != nums.end())
      for (size_t j = pow(i, 2) - 2; j <= nums.size(); j += i)
        nums[j] = 0;

  nums.erase(remove_if(nums.begin(), nums.end(), [](int i) { return i == 0; }),
             nums.end());
  return nums;
}
