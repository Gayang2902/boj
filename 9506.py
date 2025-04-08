'''[약수들의 합]
어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.
'''

def solution():
    while (num := int(input())) != -1:
        # divisors = list()
        # for i in range(1, num):
        #     if num % i == 0:
        #         divisors.append(i)
        divisors = [i for i in range(1, num) if num % i == 0]

        if sum(divisors) == num:
            print(f'{num} = ' + ' + '.join(map(str, divisors)))
        else:
            print(f'{num} is NOT perfect.')

solution()