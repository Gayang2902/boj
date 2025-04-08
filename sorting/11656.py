''' [접미사 배열]
'''

S = input()
l = []

for i in range(len(S)):
    l.append(S[i:])

print('\n'.join(sorted(l)))