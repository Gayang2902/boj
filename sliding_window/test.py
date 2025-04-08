import sys

# 입력 받기
N, d, k, c = map(int, sys.stdin.readline().split())
l = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 초밥 카운트 배열
check = [0] * (d + 1)

# 쿠폰 초밥 미리 포함 (이미 먹었다고 가정)
check[c] = 1  
eat_sushi = 1  

# 초기 윈도우 설정
for i in range(k):
    sushi = l[i]
    if check[sushi] == 0:  
        eat_sushi += 1  
    check[sushi] += 1  

max_sushi = eat_sushi  

# 슬라이딩 윈도우 실행
for i in range(N):
    # 삭제할 초밥
    start = l[i]  
    check[start] -= 1
    if check[start] == 0:
        eat_sushi -= 1  

    # 추가할 초밥 (원형 리스트 처리)
    end = l[(i + k) % N]  
    if check[end] == 0:
        eat_sushi += 1  
    check[end] += 1  

    # 최대값 갱신 (쿠폰 체크 필요 없음)
    max_sushi = max(max_sushi, eat_sushi)

print(max_sushi)
