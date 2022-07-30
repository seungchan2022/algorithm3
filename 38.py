INF = int(1e9)

n, m = map(int, input().split())
# 2차원 리스트, 모든 값 무한값
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기자신 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
# 간선 정보, 그값 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        # a -> b / b -> a 경로 존재하는지 동시 체크
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)
# 마지막 22 ~ 이해X