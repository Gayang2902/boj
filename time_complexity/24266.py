import sys

def MenOfPassion(A: list, n: int) -> int:
    sum = 0
    for i in range(1, n + 1):               #> (n)
        for j in range(1, n + 1):           #> (n)
            for k in range(1, n + 1):       #> (n)
                sum += A[i] * A[j] * A[k]
    return sum
    #> O(n^3)

n = int(sys.stdin.readline())
print('{}\n{}'.format(n ** 3, 3))