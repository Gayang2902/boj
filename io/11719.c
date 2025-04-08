#include <stdio.h>

int main(void)
{
    char s[100][101];
    int i, j;
    
    for (i = 0; i < 100 && fgets(s[i], 101, stdin); i++);
    for (j = 0; j < i; j++) {
        printf("%s", s[j]);
    }

    return 0;
}