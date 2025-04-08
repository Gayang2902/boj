''' [Z]
구간을 2 * 2까지 나눠서 구간 내에서 몇 번째인지 알아내고
Z 형태로 이동함을 이용해 이전의 방문 횟수는 그냥 x * x 형태로 알아냄
'''

N, R, C = map(int, input().split())

# Z 형태의 이동을 나타냄
dr = (0, 0, 1, 1)
dc = (0, 1, 0, 1)
rst = 0
def solve(n, r, c):
    global rst

    # 조건이 맞으면 출력 후 종료
    if r == R and c == C:
        print(rst)
        return 
    
    # 찾으려는 곳을 포함하는 구간이 아니면 n * n 구간 크기만큼 결과에 더함 (계산 생략을 하는 것)
    if not (r <= R < r + n and c <= C < c + n):
        rst += n * n
        return 
    
    # 만약 위의 조건문을 만족하지 않으면 다시 분할
    n //= 2 # 행렬을 4구간으로 분할
    for i in range(4):
        nr = r + n * dr[i]
        nc = c + n * dc[i]
        solve(n, nr, nc)

solve(2 ** N, 0, 0)