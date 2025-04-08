''' [최소공배수]
'''

def lcm(A, B):
    rst = A * B

    while B != 0:
        r = A % B
        A = B
        B = r
    
    return rst // A

T = int(input())
for i in range(T):
    print(lcm(*map(int, input().split())))