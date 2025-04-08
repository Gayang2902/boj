''' [AC]
'''

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    l = input().strip()

    if l == '[]':
        l = deque()
    else:
        l = deque(map(int, l[1:-1].split(',')))
    is_reversed = False # 회전 연산은 비용이 많이 듦... 플래그만 설정
    error = False

    for cmd in p:
        if cmd == 'R':
            is_reversed = not is_reversed
        else:
            if not l:
                print('error')
                error = True
                break
            if is_reversed:
                l.pop()
            else:
                l.popleft()
    
    if not error:
        if is_reversed:
            l.reverse()
        print('[' + ','.join(map(str, l)) + ']')