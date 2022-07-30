n = int(input())
dp = [0] * n    # 못생긴 수를 담기 위한 테이블(1차원 dp 테이블)
dp[0] = 1       # 첫 번째 못생긴 수 1

# 2배, 3배, 5배를 위한 인덱스
# 2, 3, 5의 배수 인덱스를 별도로 설정해서 n이 증가함에 따라 DP 테이블을 갱신
i2 = i3 = i5 = 0  
# 처음에 곱셈값 초기화
next2, next3, next5 = 2, 3, 5

# 1 ~ n까지 못생긴수 찾기
for k in range(1, n):
    # 가능한 곱셈 결과 중 가장 작은수 선택
    dp[k] = min(next2, next3, next5)
    # 인덱스에 따라 곱셈 결과 증가
    if dp[k] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[k] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[k] == next5:
        i5 += 1
        next5 = dp[i5] * 5
print(dp[n -1])

"""
n = int(input())
dp = [False] * (1001)
dp[0] = True

for i in range(1, 1001):
    if i % 2 == 0:
        dp[i] =True
    if i % 3 == 0:
        dp[i] = True
    if i % 5 == 0:
        dp[i] = True

result = [i for i in range(len(dp)) if dp[i] is True]
print(result[n - 1])
"""
