''' [쇠막대기]
'''

situation = input()
s = []
cnt = 0

for i in range(len(situation)):
    if situation[i] == '(':
        s.append('(')
    else:
        # 레이저라면 아직 남아있는 막대기(스택)를 전부 추가
        if situation[i - 1] == '(':
            s.pop()
            cnt += len(s)
        # 한 막대기가 끝났다면 앞에서 레이저 등에 의해 잘린 상태거나 온전한 상태 -> 조각 하나만 고려
        else:
            s.pop()
            cnt += 1

print(cnt)