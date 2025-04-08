''' [나는야 포켓몬 마스터 이다솜]
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())    
pokes = {}
for i in range(1, N + 1):
    tmp = input().rstrip()
    pokes[i] = tmp
    pokes[tmp] = i

for i in range(M):
    ques = input().rstrip()
    if ques.isdigit():
        print(pokes[int(ques)])
    else:
        print(pokes[ques])
