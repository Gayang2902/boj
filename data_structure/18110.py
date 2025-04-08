''' [solved.ac]
`아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다.`
라는 조건을 잘 봐야하는 문제
'''

import sys
input = sys.stdin.readline

N = int(input())
scores = sorted([int(input()) for _ in range(N)])

aver = int(N * 0.15 + 0.5) # 사사오입
if aver > 0:
    scores = scores[aver:-aver]
if len(scores) == 0:
    print(0)
else:
    print(int(sum(scores) / len(scores) + 0.5))