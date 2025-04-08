''' [음계]
'''

scales = list(map(int, input().split()))
t = []
for i in range(0, 7):
    t.append(scales[i] - scales[i + 1])
t = set(t)
if t == {-1}:
    print('ascending')
elif t == {1}:
    print('descending')
else:
    print('mixed')