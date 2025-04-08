''' [나무 자르기]
매개변수 탐색
'''

# 나무의 수 N, 가져가려는 나무의 길이 M
N, M = map(int, input().split())
hs = list(map(int, input().split()))
hs.sort()

left, right = 0, max(hs)
while left <= right:
    mid = (left + right) // 2
    cut = 0

    for h in hs:
        if h > mid:
            cut += h - mid

    if M <= cut:
        left = mid + 1
    else:
        right = mid - 1

print(right)