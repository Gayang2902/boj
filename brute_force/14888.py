''' [연산자 끼워넣기]
'''

from itertools import permutations

def cal(A, B, op):
    if op == '+':
        return A + B
    elif op == '-':
        return A - B
    elif op == '*':
        return A * B
    else:
        return A // B if A > 0 else -(-A // B)

N = int(input())
An = list(map(int, input().split()))
opers = list(map(int, input().split()))

opers_list = ['+'] * opers[0] + ['-'] * opers[1] + ['*'] * opers[2] + ['/'] * opers[3]
unique_opers = set(permutations(opers_list)) # 중복 순열 제거 (연산자의 모습이 동일하므로)

rst = []
for op in unique_opers:
    # 후위표기법 사용
    expr = An[0]
    for i in range(N - 1):
        expr = cal(expr, An[i + 1], op[i])
    rst.append(expr)

print(max(rst))
print(min(rst)) 