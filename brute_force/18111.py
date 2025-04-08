''' [마인크래프트]
완전 탐색 -> 브루트포스
가능한 모든 높이를 시도 (0 ~ 256)

파내는 시간은 2초, 채우는 시간은 1초로 비대칭적이기 때문에 
가능한 모든 높이에 대해 조사

문제의 조건인 `최소 시간`이라는 것이 중요
'''

# N: 세로, M: 가로, B: 시작 인벤토리 블럭 수
N, M, B = map(int, input().split())

ground = []
for _ in range(N):
    ground += list(map(int, input().split()))
min_time = float('inf')
rst_h = 0
max_h = max(ground)

for h in range(max_h + 1, -1, -1):
    p_correction = 0    # 더해야하는 값
    m_correction = 0    # 빼야하는 값

    for height in ground:
        if height < h:
            p_correction += h - height
        else:
            m_correction += height - h
    
    # 인벤토리와 파낸 값으로 가능한 경우
    if p_correction <= m_correction + B:
        time = m_correction * 2 + p_correction
        # 시간이 더 적게 걸리거나 시간은 같지만 높이가 더 높은 경우
        if time < min_time or (time == min_time and h > rst_h):
            min_time = time
            rst_h = h

print(min_time, rst_h)