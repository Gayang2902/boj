import sys

def solution():
    N = int(sys.stdin.readline())
    result = list()

    result.append(' ' * (N - 1) + '*' + '\n')
    if N > 1:
        for i in range(2, N):
            result.append(' ' * (N - i) + '*' + ' ' * (2 * i - 3) + '*' + '\n')
        result.append('*' * (2 * N - 1) + '\n') 
    sys.stdout.write(''.join(result))

solution()