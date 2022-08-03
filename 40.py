import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input())
# 시작 노드 1번 헛간
start = 1
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

# 간선 정보 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append = ((b, 1)) 
    graph[b].append = ((a, 1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 인접노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 수행
dijkstra(start)

# 최단 거리가 가장 먼 노드 번호(숨을 헛간)
max_node = 0
# 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:   # if로 하면 X
        result.append(i)
        
print(max_node, max_distance, len(result))

"""
'술래는 1번 헛간에서 출발하는데 동빈이는 1번 헛간으로부터 최단 거리가 가장 먼 헛간에 숨는다'를 보고
특정 노드에서 출발해 다른 노드를 까지의 최단 거리를 구하는 다익스트라 알고리즘 생각
'양방향 도로'이기 때문에 그래프 데이터 a, b 가 주어지면 a -> b / b -> a 모두 반영 해주어야 된다
최단 거리가 가장 긴 곳에 숨어야 하므로 최단 거리 테이블을 모두 구하고 그중에서 가장 큰 값을 구하면 된다
50 ~ 51 이해 X: 50 -> result.append(max_node) / 51 -> if ~ 가 안되는 이유?
"""
