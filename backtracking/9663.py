''' [N-Queen]
'''

import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
m = [[0] * N for _ in range(N)]

def is_possible(row, col):
    # 같은 열 검사
    for i in range(row):
        if m[i][col] == 1:
            return False
    
    # 좌측 상단 대각선 검사
    i, j = row - 1, col - 1
    while 0 <= i and 0 <= j:
        if m[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # 우측 상단 대각선 검사
    i, j = row - 1, col + 1
    while 0 <= i and j < N:
        if m[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def dfs(row):
    if row == N:
        return 1
    
    rst = 0
    # 0행에 무조건 둬도 되는 이유는 NxN 보드에서 N개 퀸을 두려면 무조건 한 행에 하나씩 둬야 하기 때문
    for col in range(N):
        if is_possible(row, col):
            m[row][col] = 1
            # 다음 행에 대해 조사
            rst += dfs(row + 1)
            m[row][col] = 0

    return rst

# print(dfs(0))

'''
하지만 좀 더 들여다 본다면, 어차피 한 행에는 무조건 하나의 퀸이 존재해야 함
이차원 배열이 아닌 일차원 배열로 퀸을 배치하고 표현하는 것이 가능
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0
으로 배치되어있다면,
1 3 0 2
로 표현하는 것이 가능하다.

같은 열에 있는지 검사
-> 배열에 같은 숫자가 존재하는지 확인
같은 대각선에 있는지 검사
-> abs(행, 행) - abs(열, 열) == 0 이리면 같은 대각선에 위치
'''

del dfs
del is_possible

# 왼쪽 대각선끼리는 row - col 값이 동일하고
# 오른쪽 대각선끼리는 row + col 값이 동일하다.
m = [0] * N
cols = [False] * N          # 같은 열에 퀸이 있는지 체크
diag1 = [False] * (2 * N)   # 왼쪽 대각선 체크 (row - col)
diag2 = [False] * (2 * N)   # 오른쪽 대각선 체크 (row + col)

def dfs(row):
    if row == N:
        return 1
    
    rst = 0
    for col in range(N):
        if cols[col] or diag1[row - col] or diag2[row + col]: # 파이썬이 음수 인덱스 접근이 가능해서 이런 방식이 가능
            continue

        cols[col] = diag1[row - col] = diag2[row + col] = True
        rst += dfs(row + 1)
        cols[col] = diag1[row - col] = diag2[row + col] = False

    return rst

print(dfs(0))