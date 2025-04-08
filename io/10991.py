import sys

def solution():
    N = int(sys.stdin.readline())

    for i in range(1, N + 1):
        stars = '*' * i
        sys.stdout.write(' ' * (N - i) + ' '.join(stars) + '\n')

solution()