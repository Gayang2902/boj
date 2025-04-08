'''[세 막대]

'''

# 삼각형의 조건: 가장 긴 변의 길이는 나머지 변들의 길이의 합보다 작아야 한다.
def solution():
    lines = list(map(int, input().split()))
    lines.sort()
    if lines[0] + lines[1] <= lines[2]:
        lines[2] = lines[0] + lines[1] - 1
        return sum(lines)
    else:
        return sum(lines)
    
print(solution())