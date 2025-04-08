#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[101];
    char ss[11] = {0, };
    size_t size;

    scanf("%100s", s);
    size = strlen(s);
    
    for (int i = 0; i < size; i += 10) {
        strncpy(ss, &s[i], 10);
        puts(ss);
        memset(ss, 0, 10);
    }

    return 0;
}