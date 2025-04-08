''' [체스판 다시 칠하기 2]
M * N 크기의 보드를 잘라 K * K 크기의 체스판으로 만들 때, 최소로 칠하는 정사각형 개수
'''

# N: 세로, M: 가로
N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]

def minimum_change(start_color):
    ps = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M):
            # 최상단과 같은 색깔을 가져야 하는 곳
            if (i + j) % 2 == 0:
                c = board[i][j] != start_color
            # 최상단과 다른 색깔을 가져야 하는 곳
            else:
                c = board[i][j] == start_color
            
            # [!] 11660번 문제의 개념을 사용
            # 인접한 곳들의 누적합을 더하고 겹치는 부분을 빼기
            ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + c

    m = 1000000000000
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            chk = ps[i + K - 1][j + K - 1] \
                - ps[i - 1][j + K - 1] \
                - ps[i + K - 1][j - 1] \
                + ps[i - 1][j - 1]
            m = min(m, chk)

    return m

print(min(minimum_change('W'), minimum_change('B')))