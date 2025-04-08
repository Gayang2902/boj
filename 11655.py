''' [ROT13]
'''

S = list(input())

changer = lambda c, o : chr(o + (ord(c) + 13 - o) % 26)

for i in range(len(S)):
    c = S[i]

    if c.isupper():
        c = changer(c, ord('A'))
        S[i] = c
    elif c.islower():
        c = changer(c, ord('a'))
        S[i] = c
    
print(''.join(S))