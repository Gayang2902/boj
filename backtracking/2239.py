''' [스도쿠]
'''

import sys
sys.setrecursionlimit(10 ** 6)

m = []
z = []
for i in range(9):
    tmp = list(map(int, input()))
    for j in range(len(tmp)):
        if tmp[j] == 0:
            z.append((i, j))
    m.append(tmp)

# 경우의 수를 측정
def cnt_possible_values(row, col):
    possible = set(range(1, 10))

    for i in range(9):
        possible.discard(m[row][i]) # 같은 행에 있는 숫자 제거
        possible.discard(m[i][col]) # 같은 열에 있는 숫자 제거

    nrow = (row // 3) * 3
    ncol = (col // 3) * 3
    for drow in range(3):
        for dcol in range(3):
            possible.discard(m[nrow + drow][ncol + dcol]) # 3x3 영역 내 숫자 제거

    return len(possible) # 남아 있는 수가 곧 경우의 수

# Using MRV
# 채울 수 있는 경우의 수가 작은 것부터 정렬
z.sort(key=lambda pos : cnt_possible_values(pos[0], pos[1]))

def is_valid(row, col, num):
    for i in range(9):
        if m[row][i] == num or m[i][col] == num:
            return False
    
    nrow = (row // 3) * 3
    ncol = (col // 3) * 3
    for dy in range(3):
        for dx in range(3):
            if m[dy + nrow][dx + ncol] == num:
                return False
            
    return True

def dfs(idx):
    if idx == len(z):
        sys.stdout.write('\n'.join(''.join(map(str, row)) for row in m) + '\n')
        exit()

    nrow, ncol = z[idx]
    for num in range(1, 10):
        # 백트래킹 시작 전에 미리 검사
        if is_valid(nrow, ncol, num):
            m[nrow][ncol] = num
            dfs(idx + 1)
            m[nrow][ncol] = 0

dfs(0)