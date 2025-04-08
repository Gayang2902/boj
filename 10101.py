'''[삼각형 외우기]

'''

def solution():
    angles = [int(input()) for _ in range(3)]

    if sum(angles) != 180:
        return 'Error'
    
    # if angles[0] == 60 and angles[1] == 60 and angles[2] == 60:
    if angles.count(60) == 3:
        return 'Equilateral'
    # elif sum(angles) == 180:
    elif len(set(angles)) == 2:
        # if angles[0] == angles[1] or angles[1] == angles[2] or angles[2] == angles[0]:
        return 'Isosceles'
    else:
        return 'Scalene'
    # else:
        # return 'Error'

print(solution())