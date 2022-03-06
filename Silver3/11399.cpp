#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> datas;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        datas.push_back(x);
    }

    sort(datas.begin(), datas.end());

    int result = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            result += datas[j];
        }
    }

    cout << result << endl;
}
