/** [분해합]
 */

#include <stdio.h>

int main(void)
{
    unsigned int N;
    unsigned int test_num;
    unsigned int test_sum;

    scanf("%d", &N);

    for (int i = 1; i <= N; i++) {
        test_num = i;
        test_sum = test_num;
        while (test_num != 0) {
            test_sum += test_num % 10;
            test_num /= 10;
        }
        if (test_sum == N) {
            printf("%u\n", i);
            return 0;
        }
    }

    puts("0");

    return 0;
}