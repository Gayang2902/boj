''' [A/B - 3]
'''

def solution(A, B):
    div = A // B
    mod = A % B
    # 파이썬에서 양수/음수를 고려한 보정작업
    if mod < 0:
        div += 1
        # 1. mod = A - (div) * B = A - divB
        # 2. mod = A - (div + 1) * B = A - divB -B
        # 3. mod = mod - B
        mod -= B

    return (div, mod)

print(f'\n'.join(str(x) for x in solution(*map(int, input().split()))))