# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 개수와 여행 계획에 속산 여행지 개수 입력
n, m = map(int, input().split())
parent = [0] * (n + 1)

# 부모를 자기 자신으로
for i in range(1, n + 1):
    parent[i] = i

# union연산 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:     # 연결된 경우 union연산
            union_parent(parent, i + 1, j + 1)

# 여행 계획
plan = list(map(int, input().split()))

result = True
# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        retult = False

# 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지(루트가 동일한지) 확인
if result:
    print('YES')
else:
    print('NO')
    
    
"""
'여행 계획'에 해당하는 모든 노드가 같은 집합에 속하기만 하면 가능한 여행 경로
따라서 두 노드 사이에 도로가 존재하는 경우 union 연산을 이용해 서로 연결된 두 노드를 같은 집합에 속하도록 만든다.
결과적으로 '여행 계획'에 포함되는 모든 노드가 모두 같은 집합에 속하는지 체크(즉, 서로소 집합)
"""    


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

graph = []
road = []   # 간선 정보
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            road.append((i + 1, j + 1))

plan = list(map(int, input().split()))

# union연산 각각 수행
for i in range(len(road)):
    a, b = road[i]
    union(parent, a, b)

# 각 원소의 루트 노드 탐색
for i in range(1, n + 1):
    find(parent, i)

result = True
for i in range(m - 1):
    # 여행 계획의 속한 모든 노드의 루트가 동일한지 확인
    if find(parent, plan[i]) != find(parent, plan[i + 1]):
        result = False

if result:
    print('YES')
else:
    print('NO')
