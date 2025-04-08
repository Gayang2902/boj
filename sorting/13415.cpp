/* deque, Ad-hoc */

#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>

using namespace std;

void solve(deque<int> &An, int A, int B)
{
    vector<int> tmp;

    // A
    for (int i = 0; i < A; i++) {
        tmp.push_back(An.front());
        An.pop_front();
    }
    sort(tmp.begin(), tmp.end());
    for (int i = A - 1; i >= 0; i--) {
        An.push_front(tmp[i]);
    }

    // B
    tmp.clear();
    for (int i = 0; i < B; i++) {
        tmp.push_back(An.front());
        An.pop_front();
    }
    if (B > A) {
        sort(tmp.begin(), tmp.end());
    }
    for (int i = 0; i < B; i++) {
        An.push_front(tmp[i]);
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N;

    deque<int> An(N);
    for (int i = 0; i < N; i++) {
        cin >> An[i];
    }

    cin >> K;
    for (int i = 0; i < K; i++) {
        int A, B;
        cin >> A >> B;
        solve(An, A, B);
    }

    for (int i = 0; i < N; i++) {
        cout << An[i] << " ";
    }
    cout << '\n';

    return 0;
}