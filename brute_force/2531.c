#include <stdio.h>
#include <string.h>

#define MAX(x, y) (x) > (y) ? (x) : (y)

int solution(int N, int d, int k, int c, int *sushis)
{
    int max_sushi = 0;
    int i, j;
    int check[3001] = {0, };
    int eat_sushi;
    int sushi;

    for (i = 0; i < N; i++) {
        memset(check, 0, d + 1);
        check[c] = 1;
        eat_sushi = 1;

        for (j = i; j < i + k; j++) {
            sushi = sushis[j % N];

            if (!check[sushi]) {
                eat_sushi++;
            }
            check[sushi]++;
        }
        max_sushi = MAX(max_sushi, eat_sushi);
    }

    return max_sushi;
}

int main(void)
{
    int N, d, k, c;
    int sushis[30000] = {0, };
    int i;

    scanf("%d %d %d %d", &N, &d, &k, &c);
    for (i = 0; i < N; i++) {
        scanf("%d", &sushis[i]);
    }

    printf("%d\n", solution(N, d, k, c, sushis));
}