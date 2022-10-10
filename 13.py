from itertools import combinations

n, m = map(int, input().split())
house = []  # 집 좌표
chicken = []    # 치킨집 좌표

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i + 1, j + 1))
        if graph[i][j] == 2:
            chicken.append((i + 1, j + 1))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합 계산 하는 함수
def sum(candidate):
    value = 0   # 도시의 치킨 거리(치킨 거리의 합)
    # 모든 집에 대해서
    for hx, hy in house:
        # 가장 가까운 치킨집 찾기
        temp = int(1e9)
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리 더하기
        value += temp
    return value

ressult = int(1e9)
for i in candidates:
    result = min(result, sum(i))

print(result)
