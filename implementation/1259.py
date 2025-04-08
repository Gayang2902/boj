''' [팰린드롬수]
'''

while True:
    test = input()
    print(exit() if int(test) == 0 else 'yes' if test == test[::-1] else 'no')