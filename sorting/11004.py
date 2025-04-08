''' [K번째 수]
'''

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

print(A[K - 1])