/* [꿀 따기]
3 <= N <= 100,000
1 <= 꿀의 양 <= 10,000
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int eat(const vector<int>& honeys, const vector<int>& ps, int i, int j, int k)
{
    // 꿀이 왼쪽 끝인 경우
    int sum_i1 = ps[j - 1] - ps[i - 1];
    int sum_i2 = ps[k - 1] - ps[i - 1] - honeys[j];
    int rst1 = sum_i1 + sum_i2;
    // j가 꿀인 경우
    int sum_j1 = ps[j] - ps[i];
    int sum_j2 = ps[k - 1] - ps[j - 1];
    int rst2 = sum_j1 + sum_j2;
    // 꿀이 오른쪽 끝인 경우
    int sum_k1 = ps[k] - ps[i] - honeys[j];
    int sum_k2 = ps[k] - ps[j];
    int rst3 = sum_k1 + sum_k2;

    return max(max(rst1, rst2), rst3);
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> honeys(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> honeys[i];
    }

    vector<int> ps(N + 1, 0);
    ps[1] = honeys[1];
    for (int i = 2; i <= N; i++) {
        ps[i] = ps[i - 1] + honeys[i];
    }

    int rst = 0;
    // 꿀의 양은 양수이기 때문에 최대의 꿀을 얻기 위해서 꿀통은 항상 양끝이어야함
    for (int j = 2; j < N; j++) {
        int temp = eat(honeys, ps, 1, j, N);
        rst = max(rst, temp);
    }

    cout << rst << endl;
    return 0;
}