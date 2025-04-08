#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    for (int i = N; i > 0; i--) {
        for (int j = i; j < N; j++) {
            printf(" ");
        }
        for (int k = i; k > 0; k--) {
            printf("*");
        }
        puts("");
    }

    return 0;
}