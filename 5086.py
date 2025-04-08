'''
약수와 배수를 판단
단순히, 나머지 값을 확인하여 풀이
'''

def solution():
    while True:
        num1, num2 = map(int, input().split())
        if num1 == 0 and num2 == 0:
            return
        if num1 % num2 == 0:
            print('multiple')
        elif num2 % num1 == 0:
            print('factor')
        else:
            print('neither')

solution()