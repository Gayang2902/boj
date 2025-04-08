''' [색종이 만들기]
1992 문제의 응용
'''

import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

rst = {0 : 0, 1 : 0}
def count_color(n, y, x):
    color = paper[y][x]

    for i in range(y, y + n):
        for j in range(x, x + n):
            if color != paper[i][j]:
                half = n // 2

                count_color(half, y, x)
                count_color(half, y, x + half)
                count_color(half, y + half, x)
                count_color(half, y + half, x + half)
                return
    
    # 덩어리를 찾으면 추가하고 종료
    rst[color] += 1

count_color(N, 0, 0)
print(rst[0])
print(rst[1])