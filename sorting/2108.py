''' [통계학]
'''

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
An = [int(input()) for _ in range(N)]

# 1. 산술평균
arithmetic_mean = round(sum(An) / N)
# 2. 중앙값
An.sort()   
median = An[N // 2]
# 3. 최빈값(귀찮으니 그냥 라이브러리 사용)
mode_count = Counter(An)
modes = sorted([k for k, v in mode_count.items() if v == max(mode_count.values())])
mode = modes[0] if len(modes) == 1 else modes[1]
# # 4. 범위
scope = max(An) - min(An)

sys.stdout.write(str(arithmetic_mean) + '\n' \
                 + str(median) + '\n' \
                 + str(mode) + '\n' \
                 + str(scope) + '\n')