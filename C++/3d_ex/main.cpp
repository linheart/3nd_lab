#include <cmath>
#include <cstddef>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

using namespace std;

vector<double> cofe(int T, int Ts, float r, int time);
pair<double, double> aprox(vector<int> x, vector<double> y);
double korrel(vector<int> x, vector<double> y);

int main() {
  int T = 88;
  int Ts = 26;
  float r_val = 0.1;
  int time = 60;

  vector<double> temperatures = cofe(T, Ts, r_val, time);
  vector<int> times = {};
  for (int i = 0; i <= time; i++)
    times.push_back(i);

  auto [a, b] = aprox(times, temperatures);
  double r = korrel(times, temperatures);

  cout << "The angular coefficient of the approximating line a: " << a << endl;
  cout << "Displacement coefficient b: " << b << endl;
  cout << "Correlation coefficient r: " << r << endl;

  for (size_t i = 0; i < temperatures.size(); i++)
    cout << "Time - " << times[i] << "c: temperature - " << temperatures[i]
         << " C" << endl;

  return 0;
}

vector<double> cofe(int T, int Ts, float r, int time) {
  vector<double> temperatures = {};
  for (int i = 0; i <= time; i++)
    temperatures.push_back(Ts + (T - Ts) * exp(-r * i));
  return temperatures;
}

pair<double, double> aprox(vector<int> x, vector<double> y) {
  size_t n = x.size();
  double xy_sum = inner_product(x.begin(), x.end(), y.begin(), 0);
  double x_sum = accumulate(x.begin(), x.end(), 0);
  double y_sum = accumulate(y.begin(), y.end(), 0);
  double x_sqr_sum = inner_product(x.begin(), x.end(), x.begin(), 0);
  double a = (n * xy_sum - x_sum * y_sum) / (n * x_sqr_sum - pow(x_sum, 2));
  double b = (y_sum - a * x_sum) / n;
  return {a, b};
}

double korrel(vector<int> x, vector<double> y) {
  double mean_x = accumulate(x.begin(), x.end(), 0.) / x.size();
  double mean_y = accumulate(y.begin(), y.end(), 0.) / y.size();
  double cov = 0.;
  double dev_x, dev_y;
  for (size_t i = 0; i < x.size(); i++) {
    cov += (x[i] - mean_x) * (y[i] - mean_y);
    dev_x += pow(x[i] - mean_x, 2);
    dev_y += pow(y[i] - mean_y, 2);
  }
  double nor = pow(dev_x * dev_y, 0.5);
  return cov / nor;
}
