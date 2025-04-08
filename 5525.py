''' [IOIOI]
KMP 알고리즘 사용
`Knuth-Morris-Pratt Algorithm`

문자열 검색 알고리즘을 좀 공부해야 할듯,,,
'''

N = int(input())
M = int(input())
S = input()

def get_pi(pattern):
    pi = [0] * len(pattern)
    i = 0
    
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = pi[i - 1]
        
        if pattern[i] == pattern[j]:
            i += 1
            pi[j] = i

    return pi

def solve(s, pattern):
    pi = get_pi(pattern)
    j = 0
    cnt = 0

    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j - 1]
        if s[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                cnt += 1
                j = pi[j - 1]
    
    return cnt

# 찾아야되는 P_N
pattern = 'O'.join(list('I' for _ in range(N + 1)))
print(solve(S, pattern))