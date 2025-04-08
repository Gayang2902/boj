#include <stdio.h>

long long solution(int N)
{
    if (N <= 1) {
        return 1;
    }
    return (long long)N * solution(N - 1);
}

int main(void)
{
    int N;
    scanf("%d", &N);

    printf("%lld\n", solution(N));

    return 0;
}