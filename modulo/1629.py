''' [곱셈] 
'''

# print(pow(*map(int, input().split())))

recur = 1
# 분할 정복으로 풀이
def solution(A, B, C):
    if B == 1:
        return A % C
    if B % 2 == 0:
        half = solution(A, B // 2, C)
        return (half * half) % C
    else:
        half = solution(A, B // 2, C)
        return (half * half * A) % C
    
print(solution(*map(int, input().split())))