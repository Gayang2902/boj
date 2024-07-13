#include <stdio.h>
#include <string.h>

int main(void)
{
    char buf[100];

    scanf("%s", buf);

    printf("%zu\n", strlen(buf));

    return 0;
}