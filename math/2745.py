''' [진법 변환]
'''

import re

N, B = input().split()

rst = 0
for i in range(len(N)):
    if re.match(r'[0-9]', N[i]):
        digit = ord(N[i]) - ord('0') # 0~9를 숫자로
    elif re.match(r'[A-Z]', N[i]):
        digit = ord(N[i]) - ord('A') + 10 # A~Z를 10~35로
    
    rst += digit * (int(B) ** (len(N) - 1 - i))

print(rst)