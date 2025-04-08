''' [랜선 자르기]
매개변수 탐색
'''

import sys
input = lambda : sys.stdin.readline()
print = lambda x: sys.stdout.write(str(x) + '\n')

K, N = map(int, input().split()) # K <= N
lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines) # 제일 긴 선을 기준선으로 선택

# N개로 나누어지는 최대 길이를 탐색하는 것이기 때문에 N개가 되었다고 종료하는 것이 아닌,
# 범위를 벗어날 때 반복문을 종료
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for line in lines:
        cnt += line // mid

    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1
    
print(end)