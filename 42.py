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
    
g = int(input())
p = int(input())
parent = [0] * (g + 1)
for i in range(1, g + 1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))    # 현재 비행기의 탑승구의 루트 확인
    if data == 0:   # 현재 루트가 0이라면, 종료
        break
    union_parent(parent, data, data - 1)    # 그렇지 않으면 바로 왼쪽의 집합과 합치기
    result += 1

print(result)

"""
각 탑승구를 서로 다른 집합으로 보자
비행기가 순서대로 들어오면 차례대로 도킹을 수행해야 하는데, 가능한 큰 번호의 탑승구로 도킹을 수행한다고 가정
이때, 도킹하는 과정을 탑승구 간 union 연산으로 이해
새롭게 비행기가 도킹이 되면, 해당 집합을 바로 왼쪽에 있는 집합과 합친다.
단, 집합의 루트가 0이면 더 이상 도킹이 불가능한 것으로 판단
항상 부모 테이블을 만들 때, 0번 루트 노드가 자동으로 생기는데 해당 문제에서 특정 탑승구 번호를 부여 받았을때,
find 연산을 수행해서 0번 루트 노드이면 더 이상 도킹할 수 없다고 만듬
"""
