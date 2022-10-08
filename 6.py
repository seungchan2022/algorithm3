import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        # 음식시간을 우선순위로 정할 것이므로 (음식시간, 음식번호)의 튜플 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0   # 그동안 먹었던 음식의 총 시간
    previous = 0    # 직전에 다 먹은 음식 시간
    length = len(food_times)    # 남은 음식 개수

    # sum_value + (이제 먹을 음식 시간 - 직전에 먹은 음식 시간) * 남은 음식 개수 -> 직전에 먹은 음식 시간을 빼주는 이유는 회전판이 돌 동안 이제 먹을 음식을 일부 먹었을 것이므로
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]   # 이제 먹을 음식 시간
        sum_value += (now - previous) * length  # 이제 먹을 음식 중 남은 시간 * 남은 음식 개수
        length -= 1     # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    result = sorted(q, key=lambda x: x[1])  # 음식 번호순 으로정렬
    return result[(k - sum_value) % length][1]  # 음식 번호 출력


"""
음식을 먹는 데 가장 적게 드는 비용의 음식부터 먹는데, 이때 회전판으로 음식이 돌아가기 때문에
한 음식을 다 먹는다고 하면 다 먹는 과정을 거치는 동안 다른 음식들도 1초씩 무조건 먹어야 한다.
그러므로 이제 먹을 음식의 시간을 계산 할 때, 직전에 먹었던 음식을 먹는데 소요되는 시간을 빼주어야 한다.
"""