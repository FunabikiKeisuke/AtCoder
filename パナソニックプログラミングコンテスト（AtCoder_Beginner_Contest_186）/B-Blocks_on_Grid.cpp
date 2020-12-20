#include <iostream>
#include <vector>
using namespace std;

int main() {
  int input_h, input_w;
  cin >> input_h >> input_w;
  vector a(input_h, vector<int>(input_w));
  for (int i = 0; i < input_h; i++) {
    for (int j = 0; j < input_w; j++) {
      cin >> a[i][j];
    }
  }

  int mn = 1e9;
  for (int i = 0; i < input_h; i++) {
    for (int j = 0; j < input_w; j++) {
      mn = min(mn, a[i][j]);
    }
  }

  int ans = 0;
  for (int i = 0; i < input_h; i++) {
    for (int j = 0; j < input_w; j++) {
      ans += a[i][j] - mn;
    }
  }

  cout << ans << endl;
  return 0;
}
