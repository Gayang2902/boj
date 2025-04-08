#include <stdio.h>

char *yo[] = {
    "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"
};

int main(void)
{
    int x, y;
    int s = 0;
    scanf("%d %d", &x, &y);

    for (int i = 1; i < x; i++) {
        if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12) {
            s += 31;
        } else if (i == 2) {
            s += 28;
        } else {
            s += 30;
        }
    }
    s += y;
    printf("%s\n", yo[s % 7]);

    return 0;
}