''' [Base Conversion]
'''

A, B = map(int, input().split())
m = int(input())
digits = list(map(int, input().split()))

num = 0
rst = []
for i in range(m):
    num += A ** (m - i - 1) * digits[i]
while num > 0:
    rst.append(num % B)
    num //= B

print(' '.join(map(str, rst[::-1])))