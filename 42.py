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

g = int(input())    # 탑승구 수
p = int(input())    # 비행기 수

array = []      # 비행기가 도킹할 수 있는 탑승구 정보
for _ in range(p):
    array.append(int(input()))

parent = [i for i in range(g + 1)]

count = 0

# 현재 비행기의 루트 확인
for i in array:
    root = find(parent, i)

    # 탑승구 루트가 0이면 break
    if root == 0:
        break

    # 탑승구를 최대 번호에 도킹하고, -1 만큼 작은 탑승구를 root로(바로 왼쪽의 집합과 합치기)
    union(parent, root, root - 1)
    count += 1

print(count)


"""
각 탑승구를 서로 다른 집합으로 보자
비행기가 순서대로 들어오면 차례대로 도킹을 수행해야 하는데, 가능한 큰 번호의 탑승구로 도킹을 수행한다고 가정
이때, 도킹하는 과정을 탑승구 간 union 연산으로 이해
새롭게 비행기가 도킹이 되면, 해당 집합을 바로 왼쪽에 있는 집합과 합친다.
단, 집합의 루트가 0이면 더 이상 도킹이 불가능한 것으로 판단
항상 부모 테이블을 만들 때, 0번 루트 노드가 자동으로 생기는데 해당 문제에서 특정 탑승구 번호를 부여 받았을때,
find 연산을 수행해서 0번 루트 노드이면 더 이상 도킹할 수 없다고 만듬
"""

# https://velog.io/@thguss/%EC%BD%94%ED%85%8C-%EC%8A%A4%ED%84%B0%EB%94%94-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%9D%B4%EB%A1%A0-%ED%83%91%EC%8A%B9%EA%B5%AC
