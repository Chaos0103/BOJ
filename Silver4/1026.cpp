#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> arrA, arrB;

bool compare(int a, int b){
    return a > b;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arrA.push_back(x);
    }

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arrB.push_back(x);
    }

    sort(arrA.begin(), arrA.end());
    sort(arrB.begin(), arrB.end(), compare);

    int result = 0;
    for (int i = 0; i < n; i++) {
        result += arrA[i] * arrB[i];
    }

    cout << result << endl;
}
