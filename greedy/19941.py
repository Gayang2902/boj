''' [햄버거 분배]
'''

def solution(N, K, A):
    cnt = 0

    for i in range(N):
        if A[i] == 'H':
            continue
        # 뒷사람을 위해 앞사람들이 뒷사람들에게서 가장 먼 (여기서는 왼쪽) 햄버거를 먹어주어야 함
        for j in range(i - K, i + K + 1):
            if 0 <= j < N:
                if A[j] == 'H':
                    A[j] = '-'
                    cnt += 1
                    break

    return cnt

N, K = map(int, input().split())
A = list(input())
print(solution(N, K, A))