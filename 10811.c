#include <stdio.h>

int main(void)
{
    int n, m;
    int i, j;
    int f, l;
    int temp;
    int array[100];

    for (int a = 0; a < 100; a++) {
        array[a] = a + 1;
    }

    scanf("%d %d", &n, &m);

    for (int a = 0; a < m; a++) {
        scanf("%d %d", &i, &j);
        f = i - 1;
        l = j - 1;
        for (int b = 0; b < (j - i + 1) / 2; b++) {
            temp = array[f];
            array[f++] = array[l];
            array[l--] = temp;
        }
    }

    for (int a = 0; a < n; a++) {
        printf("%d ", array[a]);
    }

    return 0;
}