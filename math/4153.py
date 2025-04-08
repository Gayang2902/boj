''' [직각삼각형]
'''

def solve(x, y, z):
    if x == y == z == 0:
        exit()

    n = [x, y, z]
    l = max(n)
    n.remove(l)

    if n[0] ** 2 + n[1] ** 2 == l ** 2:
        print('right')
    else:
        print('wrong')

while True:
    solve(*map(int, input().split()))