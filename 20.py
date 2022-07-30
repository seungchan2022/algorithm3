# 3개의 장애물이 설치되는 모든 조합마다(최악의경우 36C3)
# 'T'의 위치좌표를 하나씩 확인하고 'S'가 감시되는지 확인!

from itertools import combinations

n = int(input())
graph = []  # 맵 정보
teachers = []    
students = []
spaces = []

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'S':
            students.append((i, j))
        if graph[i][j] == 'T':
            teachers.append((i, j))
        # 장애물 설치할 수 있는 위치 저장
        if graph[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시(학생 발견:True, 미발견:False)
def watch(x, y, direction):
    if direction == 0:  # 왼쪽 방향 감시
        while y >= 0:
            if graph[x][y] == 'S':  # 학생 발견
                return True
            if graph[x][y] == 'O':  # 장애물 발견
                return False
            y -= 1
    if direction == 1:  # 오른쪽 방향 감시
        while y < n:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            y += 1
    if direction == 2:  # 위쪽 방향 감시
        while x >= 0:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:  # 아래쪽 방향 감시
        while x < n:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x += 1
    return False    # 좌표가 맵 밖으로 나가면

# 장애물 설치이후, 한명이라도 학생이 감지 되는지 검사
def process():
    # 모든 선생님 위치 확인
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

# 학생이 한명도 감지 되지 않도록 설치할 수 있는지 여부
find = False

# 빈공간에서 3개 뽑는 모든 조합 확인
for data in combinations(spaces, 3):
    # 1.장애물 설치
    for x, y in data:
        graph[x][y] = 'O'
    # 2. 학생 한명도 감지X
    if not process():
        find = True
        break
    # 3.장애물 제거
    for x, y in data:
        graph[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')