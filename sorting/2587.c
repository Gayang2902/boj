/* [대표값2]
 *
 */

#include <stdio.h>

int average(int *a)
{
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += a[i];
    }
    return sum / 5;
}

int middle(int *a)
{
    int m;
    int t;
    
    for (int i = 0; i < 4; i++) {
        m = i;
        for (int j = i + 1; j < 5; j++) {
            if (a[j] < a[m]) {
                m = j;
            }
        }
        t = a[m];
        a[m] = a[i];
        a[i] = t;
    }   

    return a[2];
}

int main(void)
{
    int array[5];
    int i;

    for (i = 0; i < 5; i++) {
        scanf("%d", &array[i]);
    }
    printf("%d\n", average(array));
    printf("%d\n", middle(array));

    return 0; 
}