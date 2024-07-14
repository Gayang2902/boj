#!/usr/bin/env python3

def solve():
    n, m = map(int, input().split())
    matrix1 = list()
    matrix2 = list()
    
    for _ in range(n):
        matrix1.append(list(map(int, input().split())))
    for _ in range(n):
        matrix2.append(list(map(int, input().split())))
    
    for row in range(n):
        for col in range(m):
            print(f"{matrix1[row][col] + matrix2[row][col]}", end=' ')
        print('')
        
solve()        