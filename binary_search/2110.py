''' [공유기 설치]
매개변수 탐색
'''

N, C = map(int, input().split())
xs = [int(input()) for _ in range(N)]
xs.sort()

left, right = 1, max(xs) - min(xs)
rst = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    pre = xs[0]

    for i in range(1, N):
        # 이전에 설치한 곳과의 거리가 mid 보다 크거나 같다면
        if xs[i] - pre >= mid:
            cnt += 1
            pre = xs[i] # 공유기 설치 지점
    
    if C <= cnt:
        left = mid + 1
        rst = mid # 유효거리
    else:
        right = mid - 1

print(rst)