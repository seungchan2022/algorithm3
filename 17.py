# bfs를 이용해 해결
# 다만 번호가 낮은 바이러스 부터 증식해야 되므로
# 초기에 큐에 삽입할때 낮은 번호부터 삽입

from collections import deque

n, k = map(int, input().split())

graph = []      # 전체 맵 리스트
data = []       # 바이러스 정보 

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, X좌표, Y좌표) 삽입
            data.append((graph[i][j], 0, i, j))

# 바이러스 번호가 낮은 순으로 정렬
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
    virus, s, x, y = q.popleft()
    # s초가 지나거나, 큐가 빌때 까지 반복
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이동할수 있는 경우
        if 0 <= nx < n and 0 <= ny < n:
            # 아직 방문하지 않았다면
            if graph[nx][ny] == 0:
                # 바이러스 전파
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])