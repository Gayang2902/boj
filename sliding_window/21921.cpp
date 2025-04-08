/* [블로그]
*/

#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main(void)
{
    int N, X;
    long long max_sum;
    long long sliding_window;
    int max_cnt = 1;
    
    cin >> N >> X;
    vector<int> visitors(N, 0);

    for (int i = 0; i < N; i++) {
        cin >> visitors[i];
    }
    sliding_window = accumulate(visitors.begin(), visitors.begin() + X, 0);
    max_sum = sliding_window;

    for (int i = X; i < N; i++) {
        sliding_window -= visitors[i - X];
        sliding_window += visitors[i];
        if (sliding_window == max_sum) {
            max_cnt++;
        } else if (max_sum < sliding_window) {
            max_sum = sliding_window;
            max_cnt = 1;
        }
    }

    if (max_sum == 0) {
        cout << "SAD\n";
    } else {
        cout << max_sum << '\n' << max_cnt << '\n';
    }

    return 0;
}