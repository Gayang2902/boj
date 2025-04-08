/* 숫자 카드 */

#include <stdio.h>
#include <stdlib.h>

int comp(const void *a, const void *b)
{
    int *A = (int *)a;
    int *B = (int *)b;

    if (*A > *B) return 1;
    else if (*A == *B) return 0;
    else return -1;
}

int binary_search(int *a, size_t s, int t)
{
    int first = 0;
    int last = s - 1;
    int mid;

    while (first <= last) {
        mid = (first + last) / 2;

        if (t == a[mid]) {
            return mid;
        } else {
            if (t < a[mid]) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }
    }

    return -1;
}

int main(void)
{
    int N, M;
    int i, j;
    int cards[500000];
    int numbers[500000] = {0, };
    int number;

    scanf("%d", &N);
    for (i = 0; i < N; i++) scanf("%d", &cards[i]);
    qsort(cards, N, sizeof(int), comp);

    scanf("%d", &M);
    for (i = 0; i < M; i++) {
        scanf("%d", &number);
        if (binary_search(cards, N, number) >= 0) {
            numbers[i]++;
        }
    }

    for (i = 0; i < M; i++) {
        printf("%d ", numbers[i]);
    }
    puts("");

    return 0;
}