# 중복 시그마는 안쪽에서 바깥쪽(오른쪽에서 왼쪽)으로 연산

import sys

def MenOfPassion(A: list, n: int) -> int:
    sum = 0
    global c
    for i in range(1, n - 1):               
        for j in range(i + 1, n):          
            for k in range(j + 1, n + 1):  
                c += 1
                sum += A[i] * A[j] * A[k]
    return sum

n = int(sys.stdin.readline())
c = ((n - 2) * (n - 1) * n) // 6
print('{}\n{}'.format(c, 3))