n = int(input())    # 보드의 크기
k = int(input())    # 사과의 개수
# 뱀의 머리가 뱀의 몸에 닿는 경우에도 종료해야 하므로,
# 매 시점마다 뱀이 존재하는 위치를 항상 2차원 리스트에 기록
graph = [[0] * (n + 1) for _ in range(n + 1)]
info = []   # 회전 정보 담을 리스트

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1     # 사과가 있는 위치 1로 표시

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 동 -> 남 -> 서 -> 북 순으로 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 동(0) 남(1) 서(2) 북(3) index
# 오른쪽 회전: 동(0) -> 남(1) -> 서(2) -> 북(3) -> 동(0): +1 방향
# 왼쪽 회전:동(0) -> 북(3) -> 서(2) -> 남(1) -> 동(0): -1 방향
def turn(direction, c):     # direction = 동, 서, 남, 북의 index
    if c == 'L':    # 왼쪽 회전
        direction = (direction - 1) % 4
    else:           # 오른쪽 회전
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1     # 뱀의 처음 위치
    graph[x][y] = 2 # 뱀이 존재하는 위치 2로 표시
    direction = 0   # 처음에는 동쪽을 보고 있음(index)
    time = 0        # 시작한 뒤에 지난 '초' 시간
    index = 0       # 다음에 회전할 정보
    q = [(x, y)]    # 뱀이 차지하고 있는 위치(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx <= n and 1 <= ny <= n and graph[nx][ny] != 2:
            # 사과가 없다면 이동후에 꼬리 제거
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))

                px, py = q.pop(0)   # 꼬리가 앞쪽이므로
                graph[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통에 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny   # 다음 위치로 머리 이동
        time += 1
        # 회전할 시간인 경우 회전
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
    return time

print(simulate())