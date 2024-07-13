#include <stdio.h>

int main(void)
{
    int n, m;
    int i, j;
    int temp;

    int array[100];

    for (int a = 0; a < 100; a++) {
        array[a] = a + 1;
    }

    scanf("%d %d", &n, &m);

    for (int a = 0 ; a < m; a++) {
        scanf("%d %d", &i, &j);
        temp = array[i - 1];
        array[i - 1] = array[j - 1];
        array[j - 1] = temp;        
    }

    for (int a = 0; a < n; a++) {
        printf("%d ", array[a]);
    }

    return 0;
}