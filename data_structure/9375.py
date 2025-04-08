''' [패션왕 신해빈]
어렵게 생각할 것 없이
각 종류의 갯수들의 곱 - 아무것도 안 입은 경우로 생각
'''

T = int(input())
for _ in range(T):
    d = dict()
    N = int(input())

    for _ in range(N):
        cl, ty = input().split()
        
        if ty not in d:
            d[ty] = 1
        else:
            d[ty] += 1
    
    rst = 1
    for count in d.values():
        rst *= (count + 1)
    rst -= 1 # 아무것도 안 입은 경우를 제외

    print(rst)