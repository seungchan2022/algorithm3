from collections import deque
import sys

for tc in range(int(input())):
    n = int(input())    # 노드의 개수
    indegree = [0] * (n + 1)    # 모드 노드에 대한 진입차수 0으로 초기화
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화(인접 리스트X)
    graph = [[False] * (n + 1) for i in range(n + 1)]
    # 작년 순위 정보
    data = list(map(int, input().split()))
    # 방향 그래프 간선 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            # a순위 > b순위 a -> b: b입장에서 진입차수 + 1
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    # 올해 변경된 순위 정보
    m = int(input())
    for i in range(m):
        # 작년에는 b 순위 > a 순위: a -> b로 바꾸기
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b]:
            # graph[a][b] == True라는 것은 a -> b를 의미하고 a 순위가 더 높을 의미
            # 그러므로 b -> a로 바꾸어야 함
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬 시작
    result = []
    q = deque()

    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐에서 n번 노드가 나오기 전에 큐의 원소의 길이가 0 = 사이클 발생 = 정렬 할 수 X(순위 알 수 X)
    cycle = False       # 그래프 내 사이클 존재 여부
    # 매번 큐 길이를 계산할 때, 큐 길이가 2이상(원소가 2개 이상)일때, 즉 한번에 큐에 2개 이상의 원소가 들어감 = 위상 정렬 결과 여러개
    certain = True      # 위상 정렬의 결과가 오직 하나인지의 여부

    # 정확히 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어 있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)  # 큐에서 원소를 pop하는 순서 결과 = 위상정렬 결과
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기(큐에서 빼낸 노드와 연결된 노드 탐색)
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)

    # 사이클이 발생하는 경우(일관성이 없는 경우)                
    if cycle:
        print('IM')
    # 위상 정렬 결과가 여러개인 경우
    elif not certain:
        print('?')
    # 위상 정렬 수행 결과
    else:
        for i in result:
            print(i, end=' ')
        print()


"""
- '작년 순위가 주어졌을 때, 이에 맞게 전체 팀들의 순위를 나열'
- 즉, '정해진 우선순위에 맞게 전체 팀들의 순서를 나열해야 한다' -> 위상 정렬
  그래프 데이터로 나타내기 위해서 인접 리스트가 아닌 인접 행렬을 선택했는데, 이는 올해의 상대적인 순위 정보가 주어졌을때, 
  작년 순위에서 올해 순위로 간선 방향만 바꾸어 주어 갱신 하기 위해 바로 원소에 O(1) 속도로 접근이 가능한 인접 행렬 방식을 선택
- '확실한 순위를 알 수 없는 경우'와 '일관성이 없는 데이터가 나올 경우'는 위상 정렬의 2가지 특이 케이스이다.
- 위상 정렬의 2가지 특이 케이스는 사이클이 발생한 경우와 위상 정렬 결과가 2개 이상이라는 것
1. 사이클이 발생한 경우: 큐에서 원소가 N번 나오기 전에 큐가 비는 경우, 사이클이 발생한 것으로 이해
2. 위상 정렬 결과가 2개 이상일 경우: 큐에 한번에 2개 이상의 노드가 들어갈 경우 
   즉, 매번 큐 길이를 계산 했을때 길이가 2이상이면 위상 정렬 결과가 2개 이상이라는 의미
- 그러므로 위상 정렬 수행 과정에서 큐에서 노드를 뽑을때 큐의 원소가 항상 1개로 유지되는 경우에만 고유한 순위가 존재 한다.
- 따라서 위상 정렬코드에서 매 시점마다 큐의 원소가 0개이거나, 2개 이상인지를 체크하는 부분 추가
"""
