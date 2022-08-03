# 플로이드 워셜
INF = int(1e9)
n, m = map(int, input().split())

# 2차원 리스트 만들고 모두 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선 정보
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식
for k in range(1, n+ 1):
    for a in range(1, n+ 1):
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


"""
학생들의 성적을 비교한 결과를 방향 그래프로 표현 가능 -> 최단 경로 알고리즘
학생의 수 N(노드)이 500이하의 정수이므로 플로이드 워셜 알고리즘 이용
A에서 B로 도달이 가능하거나, B에서 A로 도달이 가능하면 '성적 비교' 가능
플로이드 워셜 알고리즘을 수행한 뒤, 모든 노드에 대해 다른 노드와 서로 도달이 가능한지 체크
이때 자기 자신은 항상 도달이 가능한다고 보고, 카운트 진행
특정한 노드의 카운트 값이 N이라면, 해당 노드의 정확한 순위를 알 수 있다.
"""
