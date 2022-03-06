#include <bits/stdc++.h>

using namespace std;

int n;
vector<pair<int, int>> times;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end;
        times.push_back({start, end});
    }

    sort(times.begin(), times.end());
    int start = times[0].first;
    int end = times[0].second;
    int result = 1;
    for (int i = 1; i < n; i++) {
        if (end <= times[i].first) {
            start = times[i].first;
            end = times[i].second;
            result++;
        } else if (start <= times[i].first && times[i].second <= end) {
            start = times[i].first;
            end = times[i].second;
        }
    }

    cout << result << endl;
}
