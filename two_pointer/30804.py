''' [과일 탕후루]
오른쪽으로 이동시키면서 종류가 2개를 넘기면 왼쪽을 줄임

투 포인터라기보단 슬라이딩 윈도우의 느낌이 강함
'''

N = int(input())
stick = list(map(int, input().split()))

left = 0
cnt = dict()
mx = 0

# 오른쪽을 늘려나감
for right in range(N):
    cur = stick[right]

    if cur in cnt:
        cnt[cur] += 1
    else:
        cnt[cur] = 1

    # 만약 종류가 2개를 넘으면 왼쪽을 줄임
    while len(cnt) > 2:
        cnt[stick[left]] -= 1

        if cnt[stick[left]] == 0:
            del cnt[stick[left]]

        left += 1

    mx = max(mx, right - left + 1)

print(mx)