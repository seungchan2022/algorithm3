n = int(input())
data = []
for _ in range(n):
    data.append(list(input().split()))

data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# data = sorted(data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in data:
    print(i[0])