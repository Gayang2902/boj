'''[대지]
'''

def solution():
    N = int(input())
    dots = [list(map(int, input().split())) for _ in range(N)]
    xs, ys = zip(*dots)
    s = (max(xs) - min(xs)) * (max(ys) - min(ys))
    print(s)

solution()