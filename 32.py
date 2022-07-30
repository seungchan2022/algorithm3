n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽위에서 오는 경우
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i - 1][j - 1]
        # 바로위에서 오는 경우
        if j == i:  # 범위 벗어남
            up = 0
        else:
            up = dp[i - 1][j]
        dp[i][j] = dp[i][j] + max(left_up, up)
print(max(map(max, dp)))    # <= print(max(dp[n - 1]))
# max(map(max,dp)): 2차원 배열의 원소 중 최대값을 출력