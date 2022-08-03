INF = int(1e9)
n = int(input())
m = int(input())
# 2차원 리스트, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신 비용 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
# 간선 정보, 값 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    # 가장 짧은 간선 정보만 저장
    graph[a][b] = min(graph[a][b], c)   # if c < graph[a][b]: graph[a][b] = c
    
# 점화식 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
    
"""
전형적인 최단 경로문제
도시의 개수(노드)n이 100 이하 정수이므로 플로이드 워셜 알고리즘 이용
간선정보만 살짝 바꾸면 된다.
"""
