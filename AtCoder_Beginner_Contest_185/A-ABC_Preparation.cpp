#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  int num[4];
  for (int i = 0; i < 4; i++) {
    cin >> num[i];
  }
  sort(num, num+4);
  cout << num[0];

  return 0;
}
