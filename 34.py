n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열(LIS)' 문제로 변환
array.reverse()

# dp테이블 1로 초기화
dp = [1] * (n + 1)

for i in range(1, n):
    for j in range(i):  # 범위 잘 생각 하기
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

"""
for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
"""

# 열외시켜야 하는 병사 출력
print(n - max(dp))

"""
'가장 긴 증가하는 부분 수열(LIS 알고리즘): 하나의 수열이 주어졌을 때 값들이 증가하는 형태의 가장 긴 부분 수열 찾는 문제'
dp[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
dp[i] = max(dp[i], dp[j] + 1), if array[j] < array[i] (0 <= j < i)
위 문제는 내림차순으로 정렬해야 하므로 array를 reverse 취한다음 LIS를 풀면된다
또는 부등호를 반대로 바꾸어 주어도 된다.(15 ~ 18)
"""

# LIS 알고리즘 동작 원리
# https://techblog-history-younghunjo1.tistory.com/295
