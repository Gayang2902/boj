#include <stdio.h>

int main(void)
{
    char buf[5];

    fgets(buf, 3, stdin);
    puts(buf);

    return 0;
}