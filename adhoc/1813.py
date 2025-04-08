''' [논리학 교수]
`정확하게 i개의 말은 참이다.` 라는 말이 나타난 횟수가 i와 동일하면 참이다.
'''

N = int(input())
l = list(map(int, input().split()))

m = -1
for i in range(N + 1):
    cnt = l.count(i)
    if cnt == i:
        m = max(m, i)

print(m)