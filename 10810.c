#include <stdio.h>

int main(void)
{
    int n, m;
    int i, j, k;
    
    int array[100] = {0, };
    
    scanf("%d %d", &n, &m);
    
    for (int a = 0; a < m; a++) {
        scanf("%d %d %d", &i, &j, &k);
        for (int b = i - 1; b <= j - 1; b++) {
            array[b] = k;
        }
    }
    
    for (int a = 0; a < n; a++) {
        printf("%d ", array[a]);
    }

    return 0;
}