''' [균형잡힌 세상]
'''

while True:
    line = input()
    if line == '.':
        break

    check = []
    for l in line:
        if l == '[' or l == '(':
            check.append(l)
        elif l == ']':
            if len(check) != 0 and check[-1] == '[':
                check.pop()
            else:
                check.append(l)
                break
        elif l == ')':
            if len(check) != 0 and check[-1] == '(':
                check.pop()
            else:
                check.append(l)
                break
    if len(check) == 0:
        print('yes')
    else:
        print('no')