''' [소수의 연속합]
1. 에라토스테네스로 N 이하의 소수 집합을 확정
'''

def eratosthenes(N):
    MAX = N + 1
    # N보다 작은 소수를 구할 때는 sqrt(N) 이하의 소수들의 배수만 제거하면 됨
    LIM = int(N ** 0.5) + 1
    RSET = lambda strt, end, gap: set(range(strt, end, gap))

    # 6k - 1 | 6k + 1
    prime = RSET(5, MAX, 6) | RSET(7, MAX, 6)
    if N > 2: prime.add(3)
    if N > 1: prime.add(2)

    # 모든 소수는 6n + 1 또는 6n + 5의 형태 
    for i in range(5, LIM, 6):
        # 5 (mod 6)
        if i in prime:
            prime -= RSET(i * i, MAX, i * 6) | RSET(i * (i + 2), MAX, i * 6)
        # 1 (mod 6)
        j = i + 2
        if j in prime:
            prime -= RSET(j * j, MAX, j * 6) | RSET(j * (j + 4), MAX, j * 6)
    
    return prime

# 소수를 찾으면 해당 소수의 배수들을 리스트에서 제거해나감
def eratos(N):
    prime = [True] * (N + 1)
    prime[0] = False
    prime[1] = False

    a = []
    for i in range(2, N + 1):
        if prime[i]:
            a.append(i)
            for j in range(2, N // i + 1):
                prime[i * j] = False
    
    return a

N = int(input())
if N == 1:
    print(0)
    exit(0)

left, right = 0, 0 
p = eratos(N)
total = p[0]
cnt = 0

while left <= right:
    if total <= N:
        if total == N:
            cnt += 1

        right += 1
        if right == len(p):
            break
    
        total += p[right]
        
    elif N < total:
        total -= p[left]
        left += 1

print(cnt)