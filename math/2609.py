''' [최대공약수와 최소공배수] 
'''

def gcd(A, B):
    while B != 0:
        r = A % B
        A = B
        B = r
    
    return A

# lcm = 두 수의 곱 / gcd
def lcm(A, B):
    return (A * B) // gcd(A, B)

A, B = map(int, input().split())
print(f'{gcd(A, B)}\n{lcm(A, B)}')