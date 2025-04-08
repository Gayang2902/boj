''' [쿼드 트리]
'''

N = int(input())
image = [input() for _ in range(N)]

# n: 사각형 변의 길이, y: 시작 행, x: 시작 열
def q_tree(n, y, x):
    for i in range(y, y + n):
        for j in range(x, x + n):
            # 영역이 같지 않으면 분할탐색
            if image[y][x] != image[i][j]:
                half_n = n // 2
                
                rst = '('
                # 왼쪽 위
                rst += q_tree(half_n, y, x)
                # 오른쪽 위
                rst += q_tree(half_n, y, x + half_n)
                # 왼쪽 아래
                rst += q_tree(half_n, y + half_n, x)
                # 오른쪽 아래
                rst += q_tree(half_n, y + half_n, x + half_n)
                rst += ')'

                return rst

    return image[y][x]

print(q_tree(N, 0, 0))