#include <stdio.h>
#include <string.h>

int main(void)
{
    char buf[999];
    int num_test;

    scanf("%d", &num_test);
    for (int i = 0; i < num_test; i++) {
        scanf("%s", buf);
        printf("%c%c\n", buf[0], buf[strlen(buf) - 1]);
    }

    return 0;
}