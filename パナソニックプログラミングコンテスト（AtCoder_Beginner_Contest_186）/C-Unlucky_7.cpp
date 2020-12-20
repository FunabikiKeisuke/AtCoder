#include <iostream>
using namespace std;

int main() {
  int input_n;
  cin >> input_n;
  int ans = 0;
  for (int i = 1; i <= input_n; i++) {
    bool flag_not_7 = true;  // 問題の条件を満たしたかを判定するフラグ
    // 8 進数と 10 進数でループ
    for (int base : {8, 10}) {
      int x = i;
      while (x > 0) {
        if (x % base == 7) flag_not_7 = false; // 最小位の数が 7 かどうか判定する
        x /= base;
      }
    }
    if (flag_not_7) ans++; 
  }
  cout << ans << endl;
  return 0;
}
