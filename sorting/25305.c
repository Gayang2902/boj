/* [커트라인]
 *
 */

#include <stdio.h>
#include <stdlib.h>

// Descending Order
int comp(const void *a, const void *b)
{
    if (*(int *)a < *(int *)b) {
        return 1;
    } else if (*(int *)a > *(int *)b) {
        return -1;
    } else {
        return 0;
    }
}

int main(void)
{
    int N, k;
    int i;
    int a[1000];

    scanf("%d %d", &N, &k);
    for (i = 0; i < N; i++) {
        scanf("%d", &a[i]);
    }

    qsort(a, N, sizeof(int), comp);

    printf("%d\n", a[k - 1]);

    return 0;
}