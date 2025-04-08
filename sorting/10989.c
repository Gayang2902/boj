/* [수 정렬하기 3]
 * 카운팅 정렬을 사용하여 풀이
 */

#include <stdio.h>
#include <stdlib.h>

// 알고리즘 풀이를 위한 경량화 버전
void counting_sort(const size_t N)
{
    int c[10001] = {0, };
    int i, j;
    int num;

    for (i = 0; i < N; i++) {
        scanf("%d", &num);
        c[num]++;
    }

    for (i = 0; i < 10001; i++) {
        if (c[i] != 0) {
            for (j = 0; j < c[i]; j++) {
                printf("%d\n", i);
            } 
        }
    }
}

int main(void)
{
    int N;
    
    scanf("%d", &N);
    counting_sort(N);

    return 0;
}