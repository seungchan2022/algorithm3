def edit_dist(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]    # 2차원 dp테이블 초기화
    # dp테이블 초기 설정
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같다면, 왼쪽위에 해당하는 수 그대로 대입
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면, 3가지 경우중 최소값 + 1
            else:   # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽위)중에서 최소 비용 대입
                dp[i][j] = 1 + min(dp[i][j -1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[n][m]

a = input()
b = input()
print(edit_dist(a, b))