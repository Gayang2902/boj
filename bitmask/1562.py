''' [계단수]
길이가 N이면서 0부터 9까지 숫자가 모두 등장하는 계단 수

비트마스킹을 이용해서 0~9가 사용되었는지 확인
0b1111111111 -> 1023
모든 숫자가 사용된다면 비트마스크 숫자는 1023이 됨
'''

BIT = 1 << 10

N = int(input())
# dp[N][10][1024] == dp[digit][lsb][bit]
dp = [[[0] * BIT for _ in range(10)] for _ in range(N)]

# dp[자릿수][LSB][비트마스크]
for lsb in range(1, 10):
    dp[0][lsb][1 << lsb] = 1

for digit in range(1, N):
    for lsb in range(10):
        for bit in range(BIT):
            nxt_bit = bit | 1 << lsb

            if 0 < lsb:
                dp[digit][lsb][nxt_bit] += dp[digit - 1][lsb - 1][bit]
            if lsb < 9:
                dp[digit][lsb][nxt_bit] += dp[digit - 1][lsb + 1][bit]
            
            dp[digit][lsb][nxt_bit] %= 1_000_000_000

cnt = 0
for lsb in range(10):
    cnt += dp[N - 1][lsb][BIT - 1] # BIT - 1 = 1023
    cnt %= 1_000_000_000

print(cnt)