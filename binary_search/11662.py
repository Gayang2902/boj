''' [민호와 강호]
전형적인 삼분탐색 문제
- 두 사람은 일정한 속도로 선분을 이동
- 두 사람 간의 거리 함수 f(t)는 볼록 함수 또는 오목 함수
- 거리는 처음엔 감소하다가 어느 순간 최소값을 찍고 다시 증가 (가장 가까운 곳이 존재)
비율 t를 이용해서 어떤 t만큼 두 점이 이동했을 때, 최소지점인지 구하면 됨

절대/상대 오차는 10^{-6}까지 허용
'''

from math import sqrt

# d1에서 d2 방향으로 t 비율만큼 이동한 지점
def get_point(d1, d2, t):
    x = d1[0] + (d2[0] - d1[0]) * t
    y = d1[1] + (d2[1] - d1[1]) * t

    return (x, y)

# 두 점 사이의 거리
def distance(d1, d2):
    return sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)

# 삼분 탐색
def search(A1, A2, B1, B2):
    left, right = 0.0, 1.0
    eps = 1e-7 # 문제에서 요구하는 최소 정밀도

    while right - left > eps:
        # 전체 구간을 3등분했을 때 중간 두 지점
        t1 = (2 * left + right) / 3 # 왼쪽에서 2/3 지점
        t2 = (left + 2 * right) / 3 # 오른쪽에서 2/3 지점

        p1 = get_point(A1, A2, t1)
        q1 = get_point(B1, B2, t1)
        d1 = distance(p1, q1)

        p2 = get_point(A1, A2, t2)
        q2 = get_point(B1, B2, t2)
        d2 = distance(p2, q2)

        # 왼쪽 구간이 더 최솟값
        if d1 < d2:
            right = t2
        # 오른쪽 구간이 더 최솟값
        else:
            left = t1
    
    return distance(get_point(A1, A2, left), get_point(B1, B2, left))

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())
A1, A2 = (ax, ay), (bx, by)
B1, B2 = (cx, cy), (dx, dy)

print(f'{search(A1, A2, B1, B2):.10f}')