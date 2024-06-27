#!/usr/bin/env python3

from random import randint

def test(n: int) -> float: 
    seat = [i for i in range(n)]
    occupied = [False] * n
    
    occupied[randint(1, n)] = True
    for i in range(1, n):
        
        

def main():
    n = int(input())
    print(test(n))
    
if __name__ == '__main__':
    main()