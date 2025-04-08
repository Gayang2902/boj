''' [스타트와 링크]
'''

from itertools import combinations

N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
people = set([i for i in range(N)])
combs = combinations(people, N // 2)

rst = []
for c in combs:
    team1 = c
    team2 = people.difference(team1) # people과 team1의 차집합 = team2
    stat1 = 0
    stat2 = 0

    # 스탯 계산을 위해 2명씩 짝지어 [i][j] [j][i]를 각각 계산
    for c1, c2 in combinations(team1, 2):
        stat1 += stats[c1][c2] + stats[c2][c1]
    for c1, c2 in combinations(team2, 2):
        stat2 += stats[c1][c2] + stats[c2][c1]
    
    rst.append(abs(stat1 - stat2))

print(min(rst))    