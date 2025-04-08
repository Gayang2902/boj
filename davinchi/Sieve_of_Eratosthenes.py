''' 에라토스테네스의 체
범위 내에서 대량의 소수를 탐색하는 알고리즘 '''

def solution(N: int) -> int:
    result = [True] * (N + 1)
    result[0] = result[1] = False

    for i in range(2, N + 1):
        if result[i]:
            for j in range(i * 2, N + 1, i):
                result[j] = False

    return sum(result)

N = int(input('수의 범위를 입력해주세요> '))
print(f'2부터 {N} 까지 소수는 총 {solution(N)}개 존재합니다')