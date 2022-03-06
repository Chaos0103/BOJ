#include <bits/stdc++.h>

using namespace std;

string str;

bool re(int a, int b) {
    return a > b;
}

int main() {
    cin >> str;

    bool zero = false;
    int sum = 0;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] == '0') {
            zero = true;
        }
        sum += str[i] - '0';
    }

    if (zero && sum % 3 == 0) {
        sort(str.begin(), str.end(), re);
        for (int i = 0; i < str.size(); i++) {
            cout << str[i];
        }
    } else {
        cout << -1 << endl;
    }
}
