from collections import deque

def get_next_pos(pos, board):
    next_pos = []   # 반환 결과(로봇이 이동 가능한 위치들)
    pos = list(pos) # 현재 위치정보를 리스트로 변환(집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    
    # 상, 하, 좌, 우 이동하는 경우에 대해 처리
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하는 경우(상, 하, 좌, 우)
        # 이동하고자 하는 두 칸이 모두 비어있다면(좌표값이 모두 0인 경우 이동 가능)
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            # 튜플로 처리하고 집합으로 관리(한 번 방문한 로봇의 상태는 두번 방문하지 않는다)
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 회전하는 경우
    # 현재 로봇이 가로로 놓여있는 경우(x값이 같은 경우)
    if pos1_x == pos2_x:
        for i in [-1, 1]:   # 위쪽(-1) or 아래쪽(+1)으로 회전
            # 위, 아래행 모두 0(빈칸)이면
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여있는 경우(y값이 같은 경우)                
    elif pos1_y == pos2_y:
        for i in [-1, 1]:   # 왼쪽(-1) or 오른쪽(+1)으로 회전
            # 왼, 오른쪽 열 모두 0(빈칸)이면
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 로봇이 이동할 수있는 위치 반환
    return next_pos

def solution(board):
    # 맵의 외곽에 벽(1)을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # bfs수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}  # 로봇의 초기 위치정보(집합형태로 관리)
    q.append((pos, 0))      # 큐에 삽입한뒤 -> 튜플형태로 (로봇좌표값, 시간)삽입하는데 큐에 삽입 할때마다 시간을 + 1
    visited.append(pos)     # 방문처리
    while q:
        pos, cost = q.popleft()
        # (n, n)위치에 로봇이 도달했다면 종료
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return cost