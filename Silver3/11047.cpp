#include <bits/stdc++.h>

using namespace std;

int n, k;
vector<int> coins;

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        coins.push_back(x);
    }

    int result = 0;
    for (int i = n - 1; i > -1; i--) {
        result += k / coins[i];
        k %= coins[i];
    }

    cout << result << endl;
}
