/* [문자열 집합] 
 *
 */

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int comp(const void *a, const void *b)
{
    return strcmp(*(char **)a, *(char **)b);
}

int binary_search(const char **a, const size_t s, const char *t)
{
    int first = 0;
    int last = s - 1;
    int mid;
    int c;

    while (first <= last) {
        mid = (first + last) / 2;
        c = strcmp(a[mid], t);

        if (!c) {
            return mid;
        } else if (c < 0) {
            first = mid + 1;
        } else {
            last = mid - 1;
        }
    }
    return -1;
}

int main(void)
{
    int N, M;
    char **s;          
    char string[501];
    int sum = 0;
    int i, j;

    scanf("%d %d", &N, &M);
    s = malloc(sizeof(char *) * N);
    getchar();
    for (i = 0; i < N; i++) {
        scanf("%500s", string);
        s[i] = malloc(strlen(string));
        strncpy(s[i], string, strlen(string));
    }
    // ascending order
    qsort(s, N, sizeof(char *), comp);

    for (i = 0; i < M; i++) {
        scanf("%s", string);
        if (binary_search((const char **)s, N, string) >= 0) sum++;
    }

    printf("%d\n", sum);

    return 0;
}