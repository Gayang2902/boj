/* [수 정렬하기 2]
 */

#include <stdio.h>
#include <stdlib.h>

int comp(const void *a, const void *b)
{
    int *A = (int *)a;
    int *B = (int *)b;

    if (*A > *B) {
        return 1;
    } else if (*A < *B) {
        return -1;
    } else {
        return 0;
    }
}

int main(void)
{
    int N;
    int *a;
    int i;

    scanf("%d", &N);
    a = malloc(N * sizeof(int));
    for (i = 0; i < N; i++) {
        scanf("%d", &a[i]);
    }
    qsort(a, N, sizeof(int), comp);
    
    for (i = 0; i < N; i++) {
        printf("%d\n", a[i]);
    }

    return 0;
}