''' [반복수열]
'''

digit_sum = lambda num, P : sum(int(digit) ** P for digit in str(num))

A, P = map(int, input().split())
visited = {}
cnt = 0

# 중복된 숫자가 나타나면 반복수열이 시작된 것
while A not in visited:
    visited[A] = cnt
    cnt += 1
    A = digit_sum(A, P)

print(visited[A]) # 중복 이전까지의 수열의 길이