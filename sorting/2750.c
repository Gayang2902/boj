/* [수 정렬하기]
 * N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
 * 시간 복잡도 O(n^2)
 */

#include <stdio.h>

void solution(int *a, size_t s)
{
    int t;
    int m;

    for (int i = 0; i < s - 1; i++) {
        m = i;
        for (int j = i + 1; j < s; j++) {
            if (a[j] < a[m]) {
                m = j;
            }
        }
        t = a[i];
        a[i] = a[m];
        a[m] = t;
    }
}

int main(void)
{
    int N;
    int i;
    int a[1000];

    scanf("%d", &N);
    for (i = 0; i < N; i++) {
        scanf("%d", &a[i]);
    }
    solution(a, N);
    for (i = 0; i < N; i++) {
        printf("%d\n", a[i]);
    }

    return 0;
}