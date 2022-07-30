# 사칙연산을 중복하여 계산 -> 중복 순열
# 그러나 dfs로 풀수 있음

n = int(input())
array = list(map(int, input().split()))
# 연산자들을 리스트가 아닌 각각의 변수로 설정
add, sub, mul, div = map(int, input().split())

# m, M 초기화
min_value = int(1e9)
max_value = -int(1e9)

# i: array의 index(1부터 시작), now: 연산수행한 실시간 결과값
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:   # 각 연산을 재귀적으로 수행
        # i를 하나 증가시켜서 연산한 결과값을 넣음
        if add > 0:
            add -= 1
            dfs(i + 1, now + array[i])
            # 다른 경우도 탐색해야 하므로 원상복구
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - array[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * array[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / array[i]))    # now // array[i]로 하면 오류남
            div += 1

dfs(1, array[0])
print(max_value)
print(min_value)