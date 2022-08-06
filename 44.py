# 최소 신장트리(크루스칼)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())    # 노드
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

# 각 행성의 좌표
x = []
y = []
z = []

# 모든 노드에 대한 좌표 값
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))      # (좌표값, 인덱스)
    y.append((data[1], i))
    z.append((data[2], i))

# 좌표값이 낮은 순으로 정렬
x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(n - 1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)



"""
N - 1개의 터널을 설치해서 모든 행성이 연결되도록 -> 최소 신장 트리
임의의 두 노드 사이를 모두 측정하면 시간 초과 판정이 될수 있다.
따라서 주어진 거리 계산 공식을 활용해서 시간 초과를 해결해야 하는데,
계산 공식을 보면 x, y, z중 어떤 축이나 선택해서 그 축을 기준으로 거리를 계산해서 정렬한 것만을 가지고 최소 신장 트리를 만들 수 있다
(모든 간선 정보를 탐색하게 되면 시간초과 문제가 발생한다는 것을 캐치하면 계산 공식을 가지고 활용할 수도 있다)
x, y, z축의 값 별로 각각 리스트에 담고 정렬한후, 각 축의 좌표끼리 거리 계산을 한 후 간선 비용 정보에 담은 후 이번엔 거리(간선 비용)를
기준으로 오름차순 정렬한 다음, 간선 하나씩 화인하면서 크루스칼 알고리즘 활용
p.588 해설 보면서 이해하기
"""
