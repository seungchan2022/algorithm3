import sys
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

n, m = map(int, input().split())
parent = [0] * n
for i in range(n):
    parent[i] = i
# 모든 간선을 담을 리스트와 비용 담을 변수
edges = []
result = 0  # 최소 비용
total = 0   # 전체 비용
# 간선 정보
for _ in range(m):
    x, y, z = map(int, input().split())
    total += z
    # 비용순으로 정렬하기 위해 첫번째 원소 비용
    edges.append((z, x, y))

# 비용순으로 정렬
edges.sort()
for edge in edges:
    z, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += z

print(total - result)