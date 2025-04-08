''' [근손실]
기본적인 백트래킹 문제
'''

class solve():
    def __init__(self):
        self.N, self.K = map(int, input().split())
        self.A = list(map(int, input().split()))
        self.rst = 0
        self.visited = [False] * self.N

    def dfs(self, n, weight):

        if weight < 500:
            return
        if n == self.N:
            self.rst += 1
            return
        
        weight -= self.K
        for i in range(self.N):
            if self.visited[i]:
                continue

            self.visited[i] = True
            self.dfs(n + 1, weight + self.A[i])
            self.visited[i] = False

        return self.rst
    
s = solve()
print(s.dfs(0, 500))