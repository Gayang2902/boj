import sys

def solution():
    N = int(sys.stdin.readline())

    for i in range(1, 2 * N):
        stars = '*' * min(i, 2 * N - i)
        spaces = ' ' * (N - len(stars))
        sys.stdout.write(spaces + stars + '\n')

solution()