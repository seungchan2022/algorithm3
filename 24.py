n = int(input())

array = list(map(int, input().split()))

array.sort()
# index가 n // 2가 아니라 (n - 1) // 2 (이해 안되면 숫자 넣어보기)
result = array[(n - 1) // 2]
print(result)