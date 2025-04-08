'''약수 구하기
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

'''

def solution():
    N, K = map(int, input().split())
    magic = 0
    for i in range(1, N + 1):
        if N % i == 0:
            magic += 1
        if magic == K:
            return i
        
    return 0

print(solution())