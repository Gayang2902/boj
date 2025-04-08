/* [단어 공부]
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(void)
{
    string s;
    cin >> s;

    vector<int> a(26, 0);

    for (char c : s) {
        if (isupper(c)) {
            a[c - 'A']++;
        } else {
            a[c - 'a']++;
        }
    }

    int mv = *max_element(a.begin(), a.end());
    int mi = distance(a.begin(), max_element(a.begin(), a.end()));
    int dup = count(a.begin(), a.end(), mv);

    if (dup > 1) {
        cout << "?" << endl;
    } else {
        cout << static_cast<char>(mi + 'A') << endl;
    }

    return 0;
}