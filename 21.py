from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0  # 총 인구 이동 변수

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한뒤 데이터 갱신
def process(x, y, index):
    united = []     # 연합국가 정보 리스트
    united.append((x, y))
    q = deque()
    q.append((x, y))
    # 연합 인구를 계산할 리스트
    union[x][y] = index     # 현재 연합의 번호
    summary = graph[x][y]   # 현재 연합의 총 인구수
    count = 1               # 현재 연합의 국가수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접국가 확인
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구 분배
    for i, j in united:
        graph[i][j] = summary // count

while True:
    # 연합 처리가 되었는지 확인할 2차원 리스트(방문 리스트)
    union = [[-1] * n for _ in range(n)]
    index = 0   # 연합 ID
    # 주어진 graph 정보에서 원소 하나씩 연합 처리 시작
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1

    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    result += 1

print(result)


"""
해당 문제 풀이를 위한 핵심 단계는 다음과 같다.
1. 주어진 N by N 그래프 데이터, 연합처리용 테이블 용도로 2차원 리스트를 2개 운영했다.
   이 때, 연합처리 테이블에서는 연합 ID를 기록해서 어떤 국가(노드)들끼리 연합했는지 알 수 있게 했다.
2. 연합한 국가들 좌표를 담기 위해 리스트 1개를 운영했고 인접한 국가들 BFS 탐색하기 위해 큐 1개를 같이 운영했다.
3. 연햡 ID를 하나씩 증가시키면서 N by N 원소 하나씩 탐색하면서 모든 탐색이 끝나면 인구이동이 끝난 상태를 의미하게 되도록 설정했다. 
"""
