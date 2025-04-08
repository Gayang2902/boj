''' [큰 수 소인수분해]
'''

def solve(N):
    if N == 1:
        return 
    prime = 2
    while prime <= N and N % prime != 0:
        prime += 1
    N //= prime
    print(prime)

    return solve(N)

N = int(input())
solve(N)