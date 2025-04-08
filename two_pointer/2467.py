''' [용액]
입력되는 값들은 오름차순 정렬된 상태
맨 끝의 숫자들을 더한 값으로 초기화
1. 왼쪽을 늘리면 값이 커짐
2. 오른쪽을 줄이면 값이 작아짐
숫자의 합계가 작다면 왼쪽을 늘리고 크다면 오른쪽을 줄임
'''

N = int(input())
l = tuple(map(int, input().split()))

left, right = 0, N - 1
# 초기값
rst = abs(l[left] + l[right])
rst_left = l[left]
rst_right = l[right]

while left < right:
    tmp = l[left] + l[right]
    abs_tmp = abs(tmp)

    # 0에 더 가깝다면
    if abs_tmp < rst:
        rst = abs_tmp
        rst_left = l[left]
        rst_right = l[right]

    # 위치 조정
    if tmp < 0:
        left += 1
    else:
        right -= 1

print(rst_left, rst_right)