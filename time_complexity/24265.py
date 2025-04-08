import sys

n = int(sys.stdin.readline())
# Total sum is `Sigma of (n - i) from i equals 1 to n - 1
c = (n ** 2 - n) // 2
print('{}\n{}'.format(c, 2))
