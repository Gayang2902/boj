# n - 앞의 두 수를 더한 값이 3 이상하면 하나의 경우로 인정
#> 마지막 하나는 구하지 않아도 됨

count = 0
n = int(input())

for i in range(1, int(n / 3)):
    sum = i * 3
    
    for j in range(1, int(n / 3)):
        if n - (sum + (j * 3)) >= 3:
            count += 1
            
print(count)