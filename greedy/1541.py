''' [잃어버린 괄호]
'''

expr = input().split('-')
rst = sum(map(int, expr[0].split('+')))
for part in expr[1:]:
    rst -= sum(map(int, part.split('+')))

print(rst)