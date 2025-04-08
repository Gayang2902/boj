t = 0

def MenOfPassion(A, n):
    i = n // 2
    global t
    t += 1
    return A[i]

def solution():
    n = int(input())
    MenOfPassion([1], n)
    print(f'{t}\n0')

solution()