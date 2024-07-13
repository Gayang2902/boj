#include <stdio.h>

int main(void)
{
    char buf[1000];
    int index;

    scanf("%s", buf);
    scanf("%d", &index);

    printf("%c\n", buf[index - 1]);

    return 0;
}