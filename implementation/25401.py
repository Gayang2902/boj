''' [카드 바꾸기]
시간제한이 1.5초 > 500 * 500 이므로 브루트포싱 가능
'''

def check(index, diff, cards):
    cnt = 0
    for i in range(1, N + 1):
        index += diff
        if cards[i] != index:
            cnt += 1
    
    return cnt

def solution(N, cards):
    # N <= 3 인 경우의 서브 테스크
    if N == 2:
        return 0
    elif N == 3:
        _, a, b, c = cards
        if b - a == c - b:
            return 0
        else:
            return 1
    # 일반해: 기준이 되는 두개의 카드 선택
    rst = 500   # 2 <= N <= 500
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            # 두 수의 기준 차이는 인덱스를 고려하여 계산
            diff = (cards[j] - cards[i]) / (j - i)
            # 기준 차이가 정수가 아니라면 고려하지 않음
            if diff - int(diff) != 0:
                continue
            # 0번 인덱스(실제로는 없음)를 계산하여 check 함수에 넘겨 몇 개의 카드를 변경해야 하는지 계산
            rst = min(rst, check(cards[i] - diff * i, diff, cards))

    return rst
            
N = int(input())
cards = [0] + list(map(int, input().split()))
print(solution(N, cards))