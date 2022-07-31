n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):   # 아래에서 받는 것으로 i는 1행부터 시작
    for j in range(i + 1):  # 범위 잘 생각하기!
        # 왼쪽 위에서 오는 경우
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i - 1][j - 1]
        # 바로 위에서 오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        dp[i][j] = dp[i][j] + max(left_up, up)

print(max(map(max, dp))) # => print(max(dp[n -1]))
# max(map(max, dp)): 2차원 배열의 원소중 최대값 출력

# array변수 사용하지 않고, 바로 dp테이블에 초기 데이터를 담아 갱신
# dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
