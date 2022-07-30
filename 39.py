# 다익스트라 알고리즘(우선순위 큐)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 전체 테스트 케이스만큼 반복
for tc in range(int(input())):
    # 노드 개수
    n = int(input())
    # 맵 정보
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    # 최단 거리 테이블 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0 # 시작 위치
    # 시작노드로 가기위한 비용은 (0, 0)위치의 값으로 설정, 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 다익스트라 수행
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:   # 처리된적이 있는 노드
            continue
        for i in range(4):      # 현재 노드와 연결된 노드 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance[n - 1][n - 1])