n = int(input())
array = list(map(int, input().split()))
# 내림차순으로 정렬해야 하므로 reverse
array.reverse()

# dp 테이블 1로 초기화
dp = [1] * n

# LIS(가장 긴 증가하는 부분 수열) 수행
# 모든 0 <= j < i에 대해 dp[i] = max(dp[i], dp[j] + 1) if array[i] > array[j]
for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))