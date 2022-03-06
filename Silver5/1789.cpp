#include <bits/stdc++.h>

using namespace std;

long long n;

int main() {
    cin >> n;
    long long num = 1;
    long long sum = 1;
    while (sum <= n) {
        sum += ++num;
    }
    cout << num - 1 << endl;
}
