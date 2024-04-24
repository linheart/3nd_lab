#include <cmath>
#include <iostream>

using namespace std;

void err();
double calc_y(int x);

int main() {
  int x_start = -3;
  int x_end = 7;
  int dx;
  cout << "Input step: ";
  cin >> dx;

  if (dx <= 0)
    err();

  for (int x = x_start; x <= x_end; x += dx)
    cout << x << ' ' << calc_y(x) << endl;

  return 0;
}

void err() {
  cerr << "Invalid input" << endl;
  exit(EXIT_FAILURE);
}

double calc_y(int x) {
  if (x <= -1)
    return -x - 1;
  else if (x <= 1)
    return 0;
  else if (x <= 5)
    return pow(4 - pow(x - 3, 2), 0.5);

  return -0.5 * x + 2.5;
}
