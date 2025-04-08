''' [피보나치 수열]
'''

N = int(input())
memo = [0] * (N + 1)

# Top-Down
def fibo(n):
    if n < 2:
        return n
    
    # memoization
    if memo[n]:
        return memo[n]
    
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

print(fibo(N))

# Bottom-Up
def fibo(n):
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

print(fibo(N))