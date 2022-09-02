from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시 초기화
distance = [-1] * (n + 1)
distance[x] = 0     # 출발도시 X까지 거리는 0으로 초기화

# BFS수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인(인접 노드 탐색)
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최솟값 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
    # 최단거리가 1인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
# 만약 최단거리가 k인 도시가 없으면
if check == False:
    print(-1)
    
    
"""
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

result = []     # 거리가 같은 노드들 담을 리스트

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(v):
    q = deque()
    visited[v] += 1
    q.append(v)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)

bfs(x)

for i in range(1, n + 1):
    if visited[i] == k:
        result.append(i)

for i in result:
    if not result:
        print(-1)
    else:
        print(i)
"""
