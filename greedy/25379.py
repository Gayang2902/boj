''' [피하자]
총 4개의 경우가 존재한다.
1. 홀수들을 모두 왼쪽으로
2. 홀수들을 모두 오른쪽으로
3. 짝수들을 모두 왼쪽으로
4. 짝수들을 모두 오른쪽으로

문제에서 인접한 숫자끼리만 교환가능하기 때문에 경우의 수 축소가 가능하다.
-> 압축하면 2개의 경우가 존재
1 == 4
2 == 3
'''

def solution(N, A):
    # cnt[0] = 홀수, cnt[1] = 짝수
    cnt = [0, 0]
    # mov[0] = 홀수를 왼쪽으로, mov[1] = 짝수를 왼쪽으로
    mov = [0, 0]

    for a in A:
        idx = a % 2
        cnt[idx] += 1
        mov[idx] += cnt[1 - idx]

    return min(mov)

N = int(input())
A = list(map(int, input().split()))
print(solution(N, A))