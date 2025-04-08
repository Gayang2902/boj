#include <stdio.h>

int solution(int N, int K)
{
    int p[1001] = {0, };
    int result = 0;
    int i, j;

    for (i = 2; i <= N; i++) {
        if (p[i] == 0) {
            for (j = i; j <= N; j += i) {
                if (p[j] == 0) {
                    p[j] = 1;
                    result++;

                    if (result == K) {
                        return j;
                    }
                }
            }
        }
    }

    return 0;
}

int main(void)
{
    int N, K;

    scanf("%d %d", &N, &K);
    printf("%d\n", solution(N, K));

    return 0;
}