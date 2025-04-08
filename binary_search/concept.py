arr = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5]
def binary_search(arr, value):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2

        if arr[mid] < value:
            start = mid + 1
        else:
            end = mid
        
    return mid

print(binary_search(arr, 5))

from bisect import bisect_left, bisect_right

'''
bisect_left: 해당 값이 존재하는 인덱스를 왼쪽에서 탐색
- 해당하는 첫 번째 인덱스를 반환
bisect_right: 해당 값이 존재하는 인덱스를 오른쪽에서 탐색
- 해당하는 첫 번째 인덱스의 다음 인덱스를 반환
- 리스트의 범위를 벗어나는 값도 반환될 수 있음
'''
arr = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5]
print(bisect_left(arr, 3)) # 3
print(bisect_right(arr, 3)) # 6
print(bisect_left(arr, 5)) # 7
print(bisect_right(arr, 5)) # 10
print(bisect_right(arr, 6)) # 10