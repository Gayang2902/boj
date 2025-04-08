#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    for (int i = 1; i <= N; i++) {
        for (int j = 0; j < i; j++) printf("*");
        for (int k = 0; k < 2 * (N - i); k++) printf(" ");
        for (int j = 0; j < i; j++) printf("*");
        puts("");
    }
    for (int i = N - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) printf("*");
        for (int k = 0; k < 2 * (N - i); k++) printf(" ");
        for (int j = 0; j < i; j++) printf("*");
        puts("");
    }

    return 0;
}