#include <iostream>
#include <typeinfo>
using namespace std;

long long comb(int n, int r) {
  long long ncr = 1;
  for (int i = 1; i <= r; i++) {
    ncr *= n - i;  // nCr の分子
    ncr /= i;  // nCr の分母
  }
  return ncr;
}

int main() {
  int l_input;
  cin >> l_input;
  long long ans;
  ans = comb(l_input, 11);
  cout << ans << endl;

  return 0;
}
