#: 입력 받기
N = int(input())
a = list(map(int, input().split()))

#: 인덱스 지정
idx_a = []
for i in range(N):
    idx_a.append([i, a[i]])

#: 값을 기준으로 정렬
idx_a.sort(key=lambda x: x[1])

#: 좌표 압축
cnt = -1
tmp = float('inf')
for i in range(N):
    if tmp != idx_a[i][1]:
        cnt += 1
        tmp = idx_a[i][1]
    idx_a[i][1] = cnt

#: 인덱스 기준으로 정렬
idx_a.sort()

#: 출력하기
for _, a in idx_a:
    print(a, end=' ')
print()

