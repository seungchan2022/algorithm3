import sys

n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1                       # 집 좌표 간 최소 거리
end = array[-1] - array[0]      # 집 좌표 간 최대 거리
result = 0                      # 가장 인접한 공유기 간의 거리 기록할 변수

while start <= end:
    mid = (start + end) // 2    # 가장 인접한 공유기 사이의 거리(gap) 의미
    value = array[0]    # 가장 첫번째 집을 고정으로 하고 C - 1개 공유기를 설치하는 경우의 수를 탐색하는것
    count = 1   # 설치한 공유기 개수
    # C - 1개의 공유기를 설치하는데, 주어진 첫 번째 집 이후의 집들 부터 하나씩 설치
    # 현재 mid값을 이용해 공유기 설치
    for i in range(1, n):    # 앞에서 부터 설치
        # value = 첫 번째 집 또는 이전에 공유기 설치한 집 -> 이전 집 + 거리보다 먼지 가까운지
        if array[i] >= value + mid:
            # 해당 집에 공유기 설치
            value = array[i]
            count += 1

        # 설치한 공유기 개수가 주어진 C보다 크거나 거리가 같으면, 거리 증가
        if count >= c:
            start = mid + 1
            result = mid    # 최적의 결과 저장
        else:   # c개 이상의 공유기 설치 할 수 없는 경우, 거리 감소
            end = mid - 1
        
print(result)