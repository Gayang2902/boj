''' [소인수분해]
2부터 시작해서 나눠가기
'''

def divide_prime(num):
    if num == 1:
        return

    prime = 2
    while prime <= num and num % prime != 0:
        prime += 1

    num //= prime

    print(prime)
    return divide_prime(num)

N = int(input())
divide_prime(N)
