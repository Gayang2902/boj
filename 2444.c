#include <stdio.h>

int main(void)
{
    int n;
    
    scanf("%d", &n);

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) putchar(' ');
        for (int j = 0; j < 2 * i + 1; j++) putchar('*');
        putchar('\n');
    }

    for (int i = 0; i < 2 * n - 1; i++) putchar('*');
    putchar('\n');

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < i + 1; j++) putchar(' ');
        for (int j = 0; j < 2 * (n - i) - 3; j++) putchar('*');
        putchar('\n');
    }

    return 0;   
}