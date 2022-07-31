for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    # 2차원 테이블 초기화
    # dp 테이블과 주어진 금광 정보(array)를 하나의 배열로사용
    dp = []
    index = 0
    # 2차원 리스트에 들어갈 원소들을 1줄로 쭉 입력받아서 2차원 리스트에 넣어야 하는 부분(index 활용!!)
    for i in range(n):
        # array변수를 사용하지 않고 dp테이블에 초기 데이터를 담아 점화식에 따라 dp 테이블 갱신
        dp.append(array[index:index + m])
        index += m

    # dp 진행
    for j in range(1, m):   # 왼쪽에서 받는 입장으로 생각 하므로 j는 1열 부터 시작함
        for i in range(n):
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
            # 왼쪽 에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)

"""
array 변수는 초기 '금광' 정보를 담고 있으며, dp 변수는 다이나믹 프로그래밍을 위한 2차원 테이블
dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
단, dp 테이블에 접근해야 할 때마다 리스트 범위 체크
구현의 편의상 초기 테이블를 담는 array 변수를 사용하지 않고, 바로 dp 테이블에 초기 테이터를 담아 점화식에 따라 dp테이블 갱신
"""
