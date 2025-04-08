''' [FizzBuzz]
연속해서 문자열이 나오는 경우는 없음
무조건 숫자 정보를 포함
'''

prevs = [input() for _ in range(3)]

for i in range(3):
    if prevs[i].isdigit():
        good = int(prevs[i]) + (3 - i)

rst = ''
if good % 3 == 0:
    rst += 'Fizz'
if good % 5 == 0:
    rst += 'Buzz'
print(good if rst == '' else rst)