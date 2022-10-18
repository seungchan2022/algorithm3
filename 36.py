def edit_dist(a, b):
    n = len(a)
    m = len(b)
    # 2차원 dp테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # dp테이블 초기 설정
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같으면, 왼쪽 위에 해당하는 수 그대로 대입
            if a[i - 1] == b[j - 1]:            # a, b는 dp테이블의 인덱스가 아닌 문자열의 인덱스 이므로 -1을 해주는 것
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면, 3가지 경우중 최솟값 + 1
            else:   # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소값 + 1
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[n][m]

a = input()
b = input()
print(edit_dist(a, b))


"""
최소 편집 거리를 담을 2차원 테이블을 초기화한 뒤에, 최소 편집 거리를 계산에 테이블 갱신
점화식:
1. 두 문자가 같은 경우: dp[i][j] = dp[i - 1][j - 1]
    => 행과 열에 해당하는 문자가 서로 같다면, 위쪽 위에 해당하는 수를 그대로 삽입
2. 두 문자가 다른 경우: dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    => 행과 열에 해당하는 문자가 서로 다르다면, 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체)에 해당하는 수 중에서 가장 작은수에 + 1
"""
