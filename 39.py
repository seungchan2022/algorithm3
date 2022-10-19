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
    q = []
    distance[x][y] = graph[x][y]
    heapq.heappush(q, (graph[x][y], x, y))

    # 다익스트라 수행
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:   # 처리된적이 있는 노드
            continue
        for i in range(4):      # 현재 노드와 연결된 노드 확인(인접노드 확인)
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]     # graph[nx][ny] = 좌표값(거리값 = 비용)
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost     # cost = distance[nx][ny]로 하면 안됌(이해 X)
                heapq.heappush(q, (cost, nx, ny))   # (거리, 노드) -> (x, y)좌표 값 하나를 노드로 봄
    print(distance[n - 1][n - 1])


"""
문제에서 입력 자체가 2차원 배열로 들어기 때문에 N X N 인접 행렬을 이용해 그래프로 표현, 그래서 최단 거리 테이블도 2차원으로 표현
N의 범의가 최대 125로 작게 느낄 수 있지만, 2차원 공간이기 때문에 전체 노드의 개수는 N^2으로 10000을 넘을수 있다
따라서 플로이드 워셜 알고리즘이 아니라 다익스트라 알고리즘을 이용
(x, y)좌표 값 하나를 노드로 보는데, (x, y)에서 또 다른 (x, y)로 가는 비용은 도착하는 (x, y)좌표 값으로 한다.
ex) (1, 1) -> (1, 2)로 가는 비용은 (1, 2)좌표에 있는 값!
"""
