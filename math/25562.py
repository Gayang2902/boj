''' [차의 개수]
'''
from itertools import accumulate
N = int(input())

#: 1. 서로 다른 차의 개수의 최댓값: NC2
print(N * (N - 1) // 2)
#: 2. 서로 다른 차의 개수가 최대값이 되도록 하는 서로 다른 정수 N개
print(*list(accumulate(range(1, N), initial=1)))
#: 3. 서로 다른 차의 개수의 최솟값: 등차수열로 뽑으면 됨 -> N - 1
print(N - 1)
#: 4. 서로 다른 차의 개수가 최소값이 되도록 하는 서로 다른 정수 N개
print(*[i for i in range(1, N + 1)])
