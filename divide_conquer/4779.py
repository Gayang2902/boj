''' [칸토어 집합]
'''

def solve(n):
    if n == 1:
        return '-'
    
    # 좌/우의 형태가 동일함
    line = solve(n // 3)
    center = ' ' * (n // 3)
    return line + center + line

while True:
    try:
        N = int(input())
        print(solve(3 ** N))
    except EOFError:
        break