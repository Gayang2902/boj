''' [01타일]
점화식이 피보나치 수열의 형태
'''

N = int(input())
a, b = 1, 1 
for i in range(2, N + 1):
    a, b = b, (a + b) % 15746
print(b)