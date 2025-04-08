#include <stdio.h>

void solve(unsigned long long N)
{
    if (N == 1) {
        return;
    }

    while (N % 2 == 0) {
        puts("2");
        N /= 2;
    }
    // 소인수분해 가능한 최댓값은 sqrt(N)와 작거나 같은 값
    for (unsigned long long prime = 3; prime * prime <= N; prime += 2) {
        while (N % prime == 0) {
            printf("%llu\n", prime);
            N /= prime;
        }
    }

    if (N > 1) {
        printf("%llu\n", N);
    }
}

int main(void)
{
    unsigned long long N;
    scanf("%llu", &N);
    solve(N);

    return 0;
}