#include <iostream>
#include <vector>
using namespace std;

bool solve() {
  int n, m, t;
  cin >> n >> m >> t;
  vector<int> a(m), b(m);
  for (int i = 0; i < m; i++) {
    cin >> a[i] >> b[i];  // A, B の入力を全て受け取る
  }

  int b_prev = 0;  // 前回のループの B を保持
  int battery = n;  // バッテリー容量の最大値
  for (int i = 0; i < m; i++) {
    battery -= a[i] - b_prev;
    if (battery <= 0) {  // バッテリーが 0 以下になったら
      return false;
    }
    battery += b[i] - a[i];  // バッテリーを充電する
    if (battery > n) {  // バッテリー容量を超えて充電したら
      battery = n;  // バッテリー容量の最大値にする
    }
    b_prev = b[i];  // B の値で更新
  }
  battery -= t - b_prev;  // 家に帰るまでのバッテリー消費
  if (battery <= 0) {
    return false;
  }

  return true;
}

int main() {
  cout << (solve()? "Yes":"No") << endl;
  return 0;
}
