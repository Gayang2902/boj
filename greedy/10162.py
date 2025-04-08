''' [전자레인지]
'''

def solution(T):
    if T % 10 != 0:
        print(-1)
        exit()

    ans = [0, 0, 0]

    ans[0] = T // 300
    T %= 300
    ans[1] = T // 60
    T %= 60
    ans[2] = T // 10
    T %= 10

    return ans

T = int(input())
print(*solution(T))