import sys

def solution():
    N = int(sys.stdin.readline())

    for i in range(1, 2 * N):
        if i <= N:
            stars = '*' * (2 * N - 2 * i + 1)
        else:
            stars = '*' * (2 * i - 2 * N + 1)
        spaces = ' ' * ((2 * N - 1 - len(stars)) // 2)

        sys.stdout.write(spaces + stars + '\n')

solution()

        