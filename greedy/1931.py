''' [회의실 배정]
활동 선택 문제 알고리즘 (Activity-Selction Problem)
- 여러 가지 활동이 있을 때 어떤 사람이 수행할 수 있는 활동의 최대 갯수
'''

import sys

'''
최대한 빨리 회의가 종료되는 순으로 시간을 확보
- 회의가 끝나는 시간을 기준
1. 제일 빨리 끝나는 회의를 기준으로 겹치는 회의는 모두 제거
2. 다음으로 겹치지 않는 가장 빨리 끝나는 회의를 탐색
3. 반복
'''
def solution(N, meetings):
    # 1. 끝나는 시간을 기준으로 오름차순 정렬
    # 회의가 시작하자마자 끝나는 경우를 위해 끝나는 시간이 같다면 시작하는 시간으로 정렬
    s_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
    
    # 2. 첫 번째 회의 선택
    # 정렬되어있기 때문에 제일 먼저 시작하는 회의가 끝나는 시간이 가장 빠름
    end_time = s_meetings[0][1]
    rst = 1

    # 3. 
    for i in range(1, N):
        start_time = s_meetings[i][0]
        # 끝나는 시간보다 먼저 시작하는 회의는 넘김
        if start_time < end_time:
            continue
        end_time = s_meetings[i][1]
        rst += 1

    return rst

N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sys.stdout.write(str(solution(N, meetings)) + '\n')