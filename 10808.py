''' [알파벳 개수]
'''

S = input().strip()
dictionary = [0] * (26)
for s in S:
    dictionary[ord(s) - 97] += 1

print(*dictionary)