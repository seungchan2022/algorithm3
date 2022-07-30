
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