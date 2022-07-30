from collections import deque
import sys

for tc in range(int(input())):
    n = int(input())    # 노드 개수
    indegree = [0] * (n + 1)    # 모든 노드에 대한 진입차수 0으로 초기화
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
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
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b]: # 14 ~ 16줄 이행
            # graph[a][b] == True 라는 것은 a -> b를 의미하고 a 순위가 더 높음을 의미. 
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
    # 큐에서 n번 노드가 나오기 전에 큐의 원소 길이가 0 = 사이클 발생 = 정렬할수 X(순위 알수X)
    certain = True      # 위상 정렬 결과가 오직 하나인지의 여부
    # 매번 큐 길이를 계산할 때, 큐 길이가 2이상(원소가 2개 이상)일때, 즉 한 번에 큐에 2개 이상 원소가 들어감 = 위상 정렬 결과 여러개
    cycle = False       # 그래프 내 사이클 존재 여부

    # 정확이 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어 있다면 사이클 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)  # 큐에서 원소를 pop하는 순서 결과 = 위상정렬 결과
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기(큐에서 빼낸 노드와 연결된 노드 탐색)
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)

    # 사이클이 발생하는 경우(일관성이 없는 경우)
    if cycle:
        print('IMPOSSIBLE')
    # 위상 정렬 결과가 여러개인 경우
    elif not certain:
        print('?')
    # 위상 정렬 수행한 결과
    else:
        for i in result:
            print(i, end=' ')
        print()