#!/usr/bin/env python3

"""""""""
drunk passenger 문제에서 n번 승객의 자리를 누군가가 이미
차지하고 있을 확률을 구하는 코드 
"""""""""
def solve(n: int) -> float:
    ans: float = 1
    
    if n != 2:
        # 1번 승객이 n번 승객 자리를 고를 확률
        ans = 1.0 / (n - 1)
        ans += ((n - 2) / (n - 1)) / 2
    
    return ans

n = int(input())
print(f"{solve(n):.15f}")