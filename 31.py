# 테스트 케이스 
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 2차원 테이블 초기화
    # dp 테이블과 주어진 금광 정보를 하나의 배열로 사용
    dp = []
    index = 0
    # 2차원 리스트에 들어갈 원소들을 1줄로 쭉 입력받아서 2차원 리스트에 넣어야 하는 부분(index 활용)
    for i in range(n):
        # array변수를 사용하지 않고 dp테이블에 초기 데이터를 담아 점화식에 따라 dp 테이블 갱신
        dp.append(array[index:index + m])
        index += m
        
    # dp 진행
    for j in range(1, m):
        for i in range(1, n):
            # 왼쪽 위에서 오는 경우
            # 맨 윗 자리 -> 왼쪽 위에서 오는 값 없음
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            # 맨 아랫 자리 -> 왼쪽 아래에서 오는 값 없음
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)