''' [진법 변환 2]
'''

# 변환하고자 하는 진법으로 모듈러 연산을 하면 자릿수를 얻을 수 있음
table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int, input().split())
rst = ''

while N:
    rst += table[N % B] # digit mod (base) = (base)digit
    N //= B

print(rst[::-1])