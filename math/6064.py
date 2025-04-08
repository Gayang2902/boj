''' [카잉 달력]
중국인의 나머지 정리
복습하기
'''

import sys
input = sys.stdin.readline

def egcd(a, b):
    if b == 0:
        # a = g = a * 1 + b * 0
        return a, 1, 0

    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = (g - a * x) // b

    return g, x, y

def crt(x, y, m1, m2):
    # M, N의 최대공약수 d와 베주 항등식 계수 a, b
    d, a, b = egcd(m1, m2)
    # y - x가 gcd(m1, m2)로 나누어 떨이지지 않으면 해가 없음
    # 존재성, 유일성 검사
    if (y - x) % d != 0:
        return -1
    
    lcm = m1 * m2 // d          # 최소공배수
    mod_diff = (y - x) // d
    k = (mod_diff * a) % (m2 //d)
    sol = (k * m1 + x) % lcm

    return sol if sol != 0 else lcm

'''
sol === x (mod M)
sol === y (mod N)
'''
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    
    print(crt(x, y, M, N))