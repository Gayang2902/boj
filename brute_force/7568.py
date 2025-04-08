''' [덩치]
'''

N = int(input())
mens = [tuple(map(int, input().split())) for _ in range(N)]
for i in range(N):
    cnt = 1
    for j in range(N):
        if i != j and mens[i][0] < mens[j][0] and mens[i][1] < mens[j][1]:
            cnt += 1
    print(cnt)