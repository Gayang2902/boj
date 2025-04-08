''' [기타 레슨]
직관을 믿으면 안되는 문제
이분탐색을 사용하는 좋은 예시
'''

import sys
input = lambda : sys.stdin.readline()
print = lambda x : sys.stdout.write(str(x) + '\n')

# 강의의 수 N, 블루레이의 수 M
N, M = map(int, input().split())
l = list(map(int, input().split()))

# 가능한 블루레이 크기 중 가장 작은 값은 `가장 긴 영상 하나의 크기`
# 가능한 블루레이 크기 중 가장 큰 값은 `모든 영상의 크기를 합친 값`
left, right = max(l), sum(l)
while left <= right:
    mid = (left + right) // 2
    cnt, total = 1, 0
    for d in l:
        if total + d <= mid:
            total += d
        else:
            total = d
            cnt += 1

    if M < cnt:
        left = mid + 1
    else:
        right = mid - 1

print(left)