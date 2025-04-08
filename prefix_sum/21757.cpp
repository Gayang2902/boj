/* [나누기]
*/

#include <iostream>
#include <vector>

using namespace std;

// Dynamic Programming
int solution(int N, const vector<int>& l)
{
    long long total = 0;
    vector<long long> ps(N, 0);
    int i, j;

    for (i = 0; i < N; i++) {
        total += l[i];
        ps[i] = total;
    }

    if (total % 4 != 0) {
        return 0;
    }

    vector<int> dp(4, 0);
    dp[0] = 1;
    long long quater = total / 4;

    for (i = 0; i < N - 1; i++) {
        for (j = 3; j > 0; j--) {
            if (ps[i] == quater * j) {
                dp[j] += dp[j - 1];
            }
        }
    }

    return dp[3];
}

// Mine
int solve(int N, const vector<int> &l)
{
    long long total = 0;
    vector<long long> ps(N, 0);
    int i, j, k;
    int rst = 0;

    for (i = 0; i < N; i++) {
        total += l[i];
        ps[i] = total;
    }

    if (total % 4 != 0) {
        return rst;
    }

    for (i = 0; i < N - 3; i++) {
        if (ps[i] == total / 4) {
            for (j = i + 1; j < N - 2; j++) {
                if (ps[j] == total / 2) {
                    for (k = j + 1; k < N - 1; k++) {
                        if (ps[k] == total / 4 * 3) {
                            rst++;
                        }
                    }
                }
            }
        }
    }

    return rst;
}

int main(void)
{   
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> l(N);
    for (int i = 0; i < N; i++) {
        cin >> l[i];
    }
    cout << solve(N , l) << endl;

    return 0;
} 