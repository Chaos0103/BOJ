#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> loops;

bool re(int a, int b) {
    return a > b;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        loops.push_back(x);
    }
    sort(loops.begin(), loops.end(), re);
    int cnt = 1;
    int result = loops[0];
    for (int i = 0; i < n; i++) {
        result = max(result, loops[i] * cnt);
        cnt++;
    }

    cout << result << endl;
}
