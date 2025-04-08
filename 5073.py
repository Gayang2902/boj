'''[삼각형과 세 변]

'''

def solution():
    while sum((lines := list(map(int, input().split())))) != 0:
        lines.sort()
        if lines[0] + lines[1] <= lines[2]:
            print('Invalid')
            continue
        
        t = len(set(lines))
        if t == 1:
            print('Equilateral')
        elif t == 2:
            print('Isosceles')
        else:
            print('Scalene')
        
solution()