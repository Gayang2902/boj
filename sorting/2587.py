'''[대표값2]

'''

l = [int(input()) for _ in range(5)]
l.sort()
print(f'{sum(l) // 5}\n{l[2]}')