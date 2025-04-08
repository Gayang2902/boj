''' [Hashing]
'''

L = int(input())
inp = input()

rst = 0
for i in range(L):
    rst += (ord(inp[i]) - ord('a') + 1) * (31 ** i)
print(rst % 1234567891)