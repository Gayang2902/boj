#include <iostream>
#include <string>
#include <vector>

using namespace std;

int M[9][9];
int z_size;
bool fnd = false;
vector<pair<int, int>> z;

bool is_possible(pair<int, int> &pos)
{
    int sqr_x = pos.first / 3;
    int sqr_y = pos.second / 3;

    for (int i = 0; i < 9; i++) {
        if (i != pos.second && M[pos.first][i] == M[pos.first][pos.second]) {   
            return false;
        }
        if (i != pos.first && M[i][pos.second] == M[pos.first][pos.second]) {
            return false;
        }
    }
    for (int i = 3 * sqr_x; i < 3 * sqr_x + 3; i++) {
        for (int j = 3 * sqr_y; j < 3 * sqr_y +3; j++) {
            if (M[i][j] == M[pos.first][pos.second] && !(i == pos.first && j == pos.second)) {
                return false;
            }
        }
    }

    return true;
}

void dfs(int num)
{
    if (num == z_size) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                cout << M[i][j];
            }
            cout << '\n';
        }
        exit(0);
    }

    for (int i = 1; i < 10; i++) {
        M[z[num].first][z[num].second] = i;
        if (is_possible(z[num])) {
            dfs(num + 1);
        }
        M[z[num].first][z[num].second] = 0;
    }
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int i = 0; i < 9; i++) {
        string str;
        cin >> str;
        for (int j = 0; j < 9; j++) {
            M[i][j] = str[j] - '0';
            if (M[i][j] == 0) {
                z.push_back({i, j});
                z_size++;
            }
        }
    }
}