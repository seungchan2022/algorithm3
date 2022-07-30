"""
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(data, left_value, right_value):
    right_index = bisect_right(data, right_value)
    left_index = bisect_left(data, left_value)
    return right_index - left_index
    
n, x = map(int, input().split())
data = list(map(int, input().split()))

count = count_by_range(data, x, x)

if count == 0:
    print(-1)
else:
    print(count)
"""

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 가장 왼쪽에 있는 타겟값 인덱스 찾는 함수
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 가장 왼쪽에 있는 값을 발견했을 경우
    if (mid == 0 or array[mid - 1] < target) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

# 가장 오른쪽에 있는 타겟값 인덱스 찾는 함수
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 가장 오른쪽에 있는 값을 발견했을 경우
    if (mid == n - 1 or array[mid + 1] > target) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)

def count_value(array, target):
    n = len(array)
    start = 0
    end = n - 1

    a = first(array, target, start, end)
    if a == None:
        return 0
    b = last(array, target, start, end)

    return b - a + 1


result = count_value(array, x)
if result == 0:
    print(-1)
else:
    print(result)