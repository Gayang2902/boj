'''[달팽이는 올라가고 싶다]
하루에 올라갈 수 있는 높이 == A - B
정상에 올라가면 미끄러지지 않으므로, 올라야 하는 높이 == V - B
-> V - B = day * (A - B)
-> day = (V - B)/(A - B)

(V - B) mod (A - B)가 0이 아닌 경우 반올림해야 하므로,
day = (V - B)/(A - B) + 1
'''

import sys

def solution():
    A, B, V = map(int, sys.stdin.readline().split())
    day = int((V - B) / (A - B))

    return day if (V - B) % (A - B) == 0 else day + 1

print(solution())