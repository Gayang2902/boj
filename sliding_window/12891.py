''' [DNA 비밀번호]
'''

S, P = map(int, input().split())
DNA = input().strip()
ACGT = list(map(int, input().split()))

chk_dna = ('A', 'C', 'G', 'T')
cnt_dna = [0] * 4

def add_dna(d):
    for i in range(4):
        if d == chk_dna[i]:
            cnt_dna[i] += 1

def del_dna(d):
    for i in range(4):
        if d == chk_dna[i]:
            cnt_dna[i] -= 1

def check_dna():
    for i in range(4):
        if cnt_dna[i] < ACGT[i]:
            return False
    return True

# 최초합 구하기
for d in DNA[:P]:
    add_dna(d)
cnt = 1 if check_dna() else 0
# 슬라이딩 윈도우
for i in range(P, S):
    add_dna(DNA[i])
    del_dna(DNA[i - P])

    if check_dna():
        cnt += 1

print(cnt)