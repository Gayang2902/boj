''' [스택]
'''

import sys

class Stack():
    def __init__(self):
        self.s = list()

    def push(self, data: int):
        self.s.append(data)

    def pop(self):
        try:
            p = self.s.pop()
            sys.stdout.write(str(p) + '\n')
        except IndexError:
            sys.stdout.write(str(-1) + '\n')

    def size(self):
        sys.stdout.write(str(len(self.s)) + '\n')

    def empty(self):
        if len(self.s) == 0:
            sys.stdout.write(str(1) + '\n')
        else:
            sys.stdout.write(str(0) + '\n')

    def top(self):
        if len(self.s) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(str(self.s[len(self.s) - 1]) + '\n')

    def command(self, c: list) -> None:
        if c[0] == 'push':
            self.push(int(c[1]))
        elif c[0] == 'pop':
            self.pop()
        elif c[0] == 'size':
            self.size()
        elif c[0] == 'empty':
            self.empty()
        elif c[0] == 'top': 
            self.top()
   
N = int(sys.stdin.readline())
s = Stack()
for _ in range(N):
    s.command(sys.stdin.readline().split())