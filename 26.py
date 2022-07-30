# 매 상황마다 항상 작은수를 선택해야 하므로 우선순위큐(heapq)이용
import heapq

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

q = []
for i in data:
    heapq.heappush(q, i)

result = 0
while len(q) != 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    sum_value = a + b
    result += sum_value
    heapq.heappush(q, sum_value)
print(result)