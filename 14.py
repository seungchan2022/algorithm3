from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려 '원형' -> '일자' 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    # 투입할 친구수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화(최댓값 정의)
    answer = len(dist) + 1
    # 0부터 length - 1까지 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의수 각각에 대하여 확인(순열)
        for friends in list(permutations(dist, len(dist))):
            # 최초의 친구 1명 투입
            count = 1
            # 처음 투입된 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약지점 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1  # 새로운 친구 투입
                    if count > len(dist):   # 친구 다썻는지 확인
                        break
                    # 추가로 투입한 친구가 처리할 수 있는 위치로 업데이트
                    position = weak[index] + friends[count - 1]
            # 다 탐색했을때의 count를 최솟값으로 업데이트                
            answer = min(answer, count)
    if answer > len(dist):      # 다 처리하기전에 친구를 다 쓴 경우
        return -1
    return answer
