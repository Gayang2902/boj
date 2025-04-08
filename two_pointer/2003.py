''' [수들의 합 2]
'''

N, M = map(int, input().split())
An = list(map(int, input().split()))

start = 0
end = 0
sum_An = 0
cnt = 0

while True:
    # 마지막 위치에 도달해도 start가 계산될 수 있도록 start를 먼저 처리
    if M <= sum_An:
        sum_An -= An[start]
        start += 1
    else:
        if end == N:
            break
        sum_An += An[end]
        end += 1
    
    if sum_An == M:
        cnt += 1
    
print(cnt)