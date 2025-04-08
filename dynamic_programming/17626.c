#include <stdio.h>
#include <string.h>

int main(void)
{
    int dp[50000 + 1];
    int N;

    memset(dp, 0x3f, sizeof(dp));
    dp[0] = 0;

    for (int i = 1; i <= 50000; i++) {
        for (int j = 1; j * j <= i; j++) {
            if (dp[i] > dp[i - j * j] + 1) {
                dp[i] = dp[i - j * j] + 1;
            }
        }
    }

    scanf("%d", &N);
    printf("%d\n", dp[N]);

    return 0;
}