n = int(input())
t = []
p = []
# dp는 i번째 날부터 마지막날까지 낼 수 있는 최대 금액을 dp테이블에 담기
dp = [0] * (n + 1)  # 1차원 dp테이블 초기화
max_value = 0   # 뒤에서 부터 계산할때, 현재까지의 최대 상담금액

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서 부터 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i     # ex) 6일에 4일짜리 상담이면 10일째부터 새로운 상담 가능
    # 상담이 기간안에 끝나는 경우
    if time <= n:
        # i일에 상담을 하게 되면 얻는 금액 + i일에 하는 상담에 소요되는 time 이후의 날짜 얻는 최대 금액
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어난 경우
    else:
        dp[i] = max_value
print(max_value)